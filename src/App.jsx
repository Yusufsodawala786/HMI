import { createBrowserRouter,RouterProvider } from "react-router-dom"
import Home from "./components/home/Home"
import RootLayout from "./pages/RootLayout"
import ErrorPage from "./pages/ErrorPage"
import Learn from "./components/learn/Learn"
import Activities from "./components/activities/Activities"
import ColorSplash from "./components/activities/ColorSplash"
import PeacePuzzles  from "./components/activities/PeacePuzzles"
import BurstBliss from "./components/activities/BurstBliss"
import Printables from "./components/printables/Printables"

const router = createBrowserRouter([
  {
    path:'/',
    element:<RootLayout />,
    errorElement:<ErrorPage />,
    children:[
      {index:true,element:<Home />},
      {
        path:'learn',
        element:<Learn />
      },
      {
        path:'activities',
        children:[
          {index:true,element:<Activities />},
          {
            path:'colorsplash',
            element:<ColorSplash />
          },
          {
            path:'peacepuzzles',
            element:<PeacePuzzles />
          },
          {
            path:'burstbliss',
            element:<BurstBliss />
          }
        
        ]
      },
      {
        path:'printables',
        element:<Printables />
      
      }
    ]
  }
])

function App() {
  return (
    <>
      <div>
        <RouterProvider router={router} />
      </div>
    </>
  )
}

export default App
