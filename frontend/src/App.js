import logo from './logo.svg';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import './App.css';
import Dashboard from './Routes/Dashboard';
import { ChakraProvider } from '@chakra-ui/react'
const App = () => {
  return (
    <ChakraProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/Dashboard" element={<Dashboard />} />
          <Route path="*" element={<Navigate to="/Dashboard" replace />} />
        </Routes>

      </BrowserRouter>
    </ChakraProvider>
  );
}

export default App;
