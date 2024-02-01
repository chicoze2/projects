import styled from "styled-components";

export const Board = styled.div`
    flex: 1;
    padding: 16px;
    border: 1px solid rgba(204, 204, 204, 0.4);
    border-radius: 16px;

    display: flex;
    flex-direction: column;
    align-items: center;

    span{
        font-size: 18px;
    }

    > header{ // somente headers filhos diretos de Board
        padding: 8px;
        font-size: 14px;
        display: flex;
        align-items: center;

        gap: 8px;

        margin-bottom: 24px;
    }
`
export const OrdersContainer = styled.div`

    // Dispor os botoes verticalmente e não lado-a-lado
    display: flex;
    flex-direction: column;
    width: 100%;

    button{
        border: 1px solid rgba(204, 204, 204, 0.4);
        border-radius: 16px;

        background: #fff;
        height: 128px;


        display: flex;
        align-items: center;
        flex-direction: column;
        justify-content: center;
        gap: 4px;

        strong{
            font-weight: 500;
        }

        span{
            font-size: 14px;
            color: #666;
        }

        & + button{ //toda vez que aparecer um &botao precedido de um botao, terá uma margem para espaçar
            margin-top: 24px;
        }

    }

`
