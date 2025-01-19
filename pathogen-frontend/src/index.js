import React from 'react';
import ReactDOM from 'react-dom/client'; // 注意这里改为 'react-dom/client'
import App from './App';
import { BrowserRouter as Router } from 'react-router-dom';
import './index.css';

// 使用 React 18 的 createRoot 方法
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router>
      <App />
    </Router>
  </React.StrictMode>
);