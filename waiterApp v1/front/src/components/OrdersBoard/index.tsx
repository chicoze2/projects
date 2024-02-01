import { useState } from "react";
import { Order } from "../../types/Order"
import { OrderModal } from "../OrderModal";
import {Board, OrdersContainer } from "./styles"

import { api } from "../../utils/api";
import { toast } from 'react-toastify';

interface OrdersBoardProps {
    icon: string;
    title: string;
    orders: Order[];
    onCancelOrder: (orderId: string) => void;
    onChangeOrderStatus: (orderId: string, status: Order['status']) => void;

}

export function OrdersBoard( {title, icon, orders, onCancelOrder, onChangeOrderStatus}: OrdersBoardProps){
    const [isModalVisible, setIsModalVisible] = useState(false);
    const [selectedOrder, setSelectedOrder] = useState<Order | null>(null) //pode ser tipo null ou Order
    const [isLoading, setIsLoading] = useState(false);

    async function handleChangeOrderStatus(){
        setIsLoading(true)

        const newStatus = selectedOrder?.status === 'WAITING'
            ? 'IN_PRODUCTION'
            : 'DONE';

        await api.patch(`/orders/${selectedOrder?._id}`, { status: newStatus})

        toast.success(`O pedido da mesa ${selectedOrder?.table} foi alterado!`);

        onChangeOrderStatus(selectedOrder!._id, newStatus)
        setIsLoading(false);
        setIsModalVisible(false);
    }

    function handleOpenModal(order: Order){
        setIsModalVisible(true)
        setSelectedOrder(order);

    }

    function handleCloseModal() {
        setIsModalVisible(false)
        setSelectedOrder(null)
    }

    async function handleCancelOrder() {
        setIsLoading(true);
        await api.delete(`/orders/${selectedOrder?._id}`)

        toast.success(`O pedido da mesa ${selectedOrder?.table} foi cancelado!`);

        setIsLoading(false);
        setIsModalVisible(false);
        onCancelOrder(selectedOrder!._id)

    }

    return (

    <Board>

        <OrderModal
            visible={isModalVisible}
            order={selectedOrder}
            onClose={handleCloseModal}
            onCancelOrder={handleCancelOrder}
            isLoading={isLoading}
            onChangeStatus={handleChangeOrderStatus}
        />

        <header>
            <span>{icon}</span>
            <strong>{title}</strong>
            <span>({orders.length})</span>
        </header>


        <OrdersContainer>
            {orders.map((order: Order)=> (
                 <button onClick={() => handleOpenModal(order)} type='button' key={order._id}>
                    <strong>Mesa {order.table}</strong>
                    <span>{order.products.length} Itens</span>
                </button>
            ))}


        </OrdersContainer>

    </Board>

    )
}
