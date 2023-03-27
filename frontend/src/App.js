import logo from './logo.svg';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import './App.css';
import Dashboard from './Routes/dashboard';
import DashboardBasic from './Routes/dashboardBasic';
import { ChakraProvider } from '@chakra-ui/react'
const App = () => {
  return (
    <ChakraProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/Dashboard" element={<Dashboard />} />
          <Route path="/DashboardBasic" element={<DashboardBasic />} />
          <Route path="*" element={<Navigate to="DashboardBasic" replace />} />
        </Routes>

      </BrowserRouter>
    </ChakraProvider>
  );
}

export default App;
