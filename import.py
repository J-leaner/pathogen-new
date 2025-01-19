import csv
import pymysql

# 数据库连接配置
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "pathogen_genome_db",
    "port": 3306
}

# 目标表名
table_name = "Genes"

# CSV 文件路径
csv_file = r"C:\Windows\System32\pathogen_backend\gene_annotations.csv"

# 插入数据的 SQL 命令
insert_query = f"""
INSERT INTO {table_name} (species_id,name, function_annotation, sequence)
VALUES (%s,%s, %s, %s)
"""

# 连接数据库并导入数据
def import_csv_to_db():
    try:
        # 连接到 MySQL 数据库
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()
        species_id=1

        # 打开 CSV 文件并逐行读取
        with open(csv_file, "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # 跳过标题行

            # 遍历 CSV 文件中的每一行
            for row in csv_reader:
                gene = row[0]  # 基因名称
                product = row[1]  # 功能注释
                location = row[2]  # 基因位置
                cursor.execute(insert_query, (species_id, gene, product, location))

        # 提交事务
        connection.commit()
        print(f"Data imported successfully from {csv_file} to {table_name}!")

    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        # 关闭数据库连接
        if connection:
            connection.close()

if __name__ == "__main__":
    import_csv_to_db()