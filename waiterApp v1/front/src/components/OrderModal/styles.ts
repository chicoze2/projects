import styled from "styled-components";

export const Overlay = styled.div`

    left: 0px;
    top: 0px;
    background: rgba(0, 0, 0, 0.8);
    backdrop-filter: blur(4.5px);


    width: 100%;
    height: 100%;
    position: fixed;

    display: flex;
    align-items:center;
    justify-content: center;

`
export const ModalBody = styled.div`

    background: #fff;
    width: 480px;
    border-radius: 8px;
    padding: 32px;

    header{
        display: flex;
        align-items: center;
        justify-content: space-between;

        strong{
            font-size: 24px
        }

        button{
            line-height: 0;
            border: 0;
            background: transparent;
        }
    }

    .status-container{
        margin-top: 32px;

        div{
            margin-top: 8px;
            display:flex;
            gap: 8px;
            align-items: center;
        }

        small{
            font-size: 14px;
            opacity: 0.8;
        }
    }

`

export const OrderDetails = styled.div`

    margin-top: 32px;

    > strong{
        font-weight: 500;
        font-size: 14px;
        opacity: 0.8px;
    }


    .order-itens{
        margin-top: 16px;

        .item{
            display: flex;

            & + .item{
                margin-top: 16px; // margin  between the 2nd and 3th chlid ...
            }

            img{
                border-radius: 6px;
            }

            .quantity{
                font-size: 14px;
                color: #666;

                display: block;
                min-width: 20px;

                margin-left: 12px;
            }

            .product-details{
                margin-left: 4px;

                strong{
                    display: block; //para deixar cada elemento em uma linha
                }

                span{
                    font-size: 14px;
                    color: #666;
                }
            }

        }
    }

    .total-info{
        display: flex;
        align-items: center;
        justify-content: space-between;

        margin-top: 24px;

        span{
            font-weight: 500;
            font-size: 14px;
            opacity: 0.8;
        }

    }
`

export const Actions = styled.div`

    margin-top: 32px;
    display: flex;
    flex-direction: column;

    .primary{
        background: #333;
        border-radius: 48px;
        border: 0;
        color: white;

        font-size: 16px;
        padding: 12px 24px;

        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
    }

    .secondary{
        padding: 12px 24px;
        margin-top: 12px;

        color: #D73035;
        background: white;

        font-weight: bold;

        border-radius: 48px;
        border: 0;
    }

    .secondary:hover{
        background: rgb(237, 240, 245);
        transition: 0.2s;

        color: black;

    }

    button:disabled{
        opacity: 0.5;
        cursor: not-allowed;
    }

`

