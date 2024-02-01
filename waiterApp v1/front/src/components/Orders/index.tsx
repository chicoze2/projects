import { useEffect, useState } from "react";
import socketIo from 'socket.io-client'
import { toast } from 'react-toastify';

import { OrdersBoard } from "../OrdersBoard"
import { Container } from "./styles"

import { Order } from "../../types/Order";
import { api } from "../../utils/api";



export function Orders(){

    const [orders, setOrders] = useState<Order[]>([])

    useEffect(() => {
        api.get("/orders").then(({data}) => {
            setOrders(data)
        })

        const socket = socketIo('http://192.168.1.100:3000', {
            transports: ['websocket']
        })

        socket.on('order@new', (data) => {
            console.log(data)
            setOrders(prevState => prevState.concat(data))

            toast.info(`Você recebeu um novo pedido: Mesa ${data.table}`)
        })

    }, [])

    const waiting = orders.filter( (order) => order.status === 'WAITING')
    const inProduction = orders.filter( (order) => order.status === 'IN_PRODUCTION')
    const done = orders.filter( (order) => order.status === 'DONE')

    function handleCancelOrder(orderId: string) {
        setOrders( (prevState) => prevState.filter(order => order._id !== orderId))
    }


    function handleOrderStatusChange(orderId: string, status: Order['status'] ){

        setOrders((prevState) => prevState.map((order) => (
            order._id === orderId
                ? {...order, status: status}
                : order
        )))

    }

    return (
        <Container>

        <OrdersBoard
            icon="🕝"
            title="Fila de Espera"
            orders={waiting}
            onCancelOrder={handleCancelOrder}
            onChangeOrderStatus={handleOrderStatusChange}
        ></OrdersBoard>
        <OrdersBoard
            icon="🧑‍🍳"
            title="Em preparação"
            orders={inProduction}
            onCancelOrder={handleCancelOrder}
            onChangeOrderStatus={handleOrderStatusChange}


            ></OrdersBoard>
        <OrdersBoard
            icon="✅"
            title="Pronto"
            orders={done}
            onCancelOrder={handleCancelOrder}
            onChangeOrderStatus={handleOrderStatusChange}


            ></OrdersBoard>

        </Container>
    )
}
