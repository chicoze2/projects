import { useEffect } from "react";
import closeIcon from "../../assets/images/close-icon.svg";
import { Order } from "../../types/Order";
import { formatCurrency } from "../../utils/formatCurrency";

import { Actions, ModalBody, OrderDetails, Overlay } from "./styles";

interface OrderModalProps {
    visible: boolean;
    order: Order | null;
    onClose(): void;
    onCancelOrder: () => Promise<void>;
    onChangeStatus(): void;
    isLoading: boolean;
}

export function OrderModal({
    visible,
    order,
    onClose,
    onCancelOrder,
    isLoading,
    onChangeStatus
}: OrderModalProps) {
    useEffect(() => {
        document.addEventListener("keydown", (event) => {
            if (event.key === "Escape") {
                onClose();
            }
        });
    });

    if (!visible || !order) {
        return null;
    }

    let total = 0;

    order.products.forEach(({ product, quantity }) => {
        total += product.price * quantity;
    });

    return (
        <Overlay>
            <ModalBody>
                <header>
                    <strong>Mesa {order.table}</strong>
                    <button type="button" onClick={onClose}>
                        <img src={closeIcon} alt="Fechar" />
                    </button>
                </header>

                <div className="status-container">
                    <small>Status do pedido</small>
                    <div>
                        <span>
                            {order.status === "WAITING" && "🕑"}
                            {order.status === "IN_PRODUCTION" && "🧑‍🍳"}
                            {order.status === "DONE" && "✅"}
                        </span>
                        <strong>
                            {order.status === "WAITING" && "Fila de espera:"}
                            {order.status === "IN_PRODUCTION" &&
                                "Em preparação:"}
                            {order.status === "DONE" && "Pronto!"}
                        </strong>
                    </div>
                </div>

                <OrderDetails>
                    <strong>Itens</strong>

                    <div className="order-itens">
                        {order.products.map(({ _id, product, quantity }) => (
                            <div className="item" key={_id}>
                                <img
                                    src={`http://192.168.1.100:3000/uploads/${product.imagePath}`}
                                    alt="Product item image"
                                    width="56"
                                    height="28"
                                />

                                <span className="quantity">{quantity}x</span>

                                <div className="product-details">
                                    <strong>{product.name}</strong>
                                    <span>{formatCurrency(product.price)}</span>
                                </div>
                            </div>
                        ))}

                        <div className="total-info">
                            <span>Total</span>
                            <strong>{formatCurrency(total)}</strong>
                        </div>
                    </div>
                </OrderDetails>

                <Actions>

                    {order.status !== 'DONE' && (
                    <button
                        type="button"
                        className="primary"
                        disabled={isLoading}
                        onClick={onChangeStatus}
                    >
                        <span>
                            {order.status === 'WAITING' && '🧑‍🍳'}
                            {order.status === 'IN_PRODUCTION' && '✅'}
                        </span>
                        <strong>
                            {order.status === 'WAITING' && 'Iniciar produção'}
                            {order.status === 'IN_PRODUCTION' && 'Concluir pedido'}
                        </strong>
                    </button>

                    )}



                    <button
                        type="button"
                        className="secondary"
                        onClick={onCancelOrder}
                        disabled={isLoading}
                    >
                        <strong>Cancelar pedido</strong>
                    </button>
                </Actions>
            </ModalBody>
        </Overlay>
    );
}
