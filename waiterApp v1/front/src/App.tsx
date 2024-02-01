import { ToastContainer } from "react-toastify"
import 'react-toastify/dist/ReactToastify.css'

import { GlobalStyles } from "./styles/GlobalStyles"

import { Header } from "./components/Header/index"
import { Orders } from "./components/Orders/index"
import { Root } from "./components/Root/styles"

export function App() {
    return (
    <Root>
        <GlobalStyles/>
        <Header/>
        <Orders/>
        <ToastContainer position="bottom-center" />
    </Root>
    )
}
