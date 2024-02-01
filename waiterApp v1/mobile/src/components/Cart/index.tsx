import React, { useState } from "react"
import { FlatList, Platform, TouchableOpacity } from "react-native"

import { Text } from "../Text"
import { CartItem } from "../../types/CartItem"

import { Item , ProductContainer, Actions, Image, QuantityContainer, ProductDetails,
	Summary, TotalContainer} from "./styles"
import { formatCurrency } from "../../utils/formatCurrency"
import { MinusCircle } from "../Icons/MinusCircle"
import { PlusCircle } from "../Icons/PlusCircle"
import { Button } from "../Button"
import { ProductType } from "../../types/product"
import { OrderConfirmedModal } from "../OrderConfirmedModal"
import { api } from "../../utils/api"

interface CartProps {
	cartItems: CartItem[];
	onAdd: (product: ProductType) => void;
	onRemove: (product: ProductType) => void;
	onConfirmOrder: () => void;
	selectedTable: string;
}

export function Cart({ cartItems, onAdd, onRemove, onConfirmOrder, selectedTable} : CartProps) {

	const [isLoading] = useState(false)
	const [isModalVisible, setModalVisible] = useState(false) /// change to false aft debug

	const isCartFilled = cartItems.length>0

	const total = cartItems.reduce((acc, CartItem) => {
		return acc + CartItem.quantity * CartItem.product.price
	}, 0)


	async function handleConfirmOrder(){
		if(isCartFilled){

			const payload = {
				name: "Francisco testebakcend", //todo get name
				table: selectedTable,
				products: cartItems.map((cartItem) => ({
					product: cartItem.product._id,
					quantity: cartItem.quantity
				}))
			}

			await api.post("/orders", payload)
			setModalVisible(true)
		}}


	return (
		<>

			<OrderConfirmedModal
				visible={isModalVisible}
				onOk={onConfirmOrder}
			/>

			{isCartFilled && (
				<FlatList
					data={cartItems}
					keyExtractor={cartItem => cartItem.product._id}
					showsVerticalScrollIndicator={false}

					style={Platform.OS === "ios" ? {paddingHorizontal: 16, maxHeight: 150} : {maxHeight: 150}}

					renderItem={({item : CartItem	}) => (
						<Item>
							<ProductContainer>
								<Image
									source={{
										uri: `http://192.168.1.100:3000/uploads/${CartItem.product.imagePath}`
									}}
								/>

								<QuantityContainer>
									<Text size={14} color='#666'>{CartItem.quantity}x</Text>

								</QuantityContainer>

								<ProductDetails>
									<Text size={14} weight="600">{CartItem.product.name}</Text>
									<Text size={14} color='#666' style={{marginTop: 4}}>{formatCurrency(CartItem.product.price)}</Text>
								</ProductDetails>





							</ProductContainer>

							<Actions>
								<TouchableOpacity
									style={{marginRight: 16}}
									onPress={() => onRemove(CartItem.product)}>
									<MinusCircle/>
								</TouchableOpacity>

								<TouchableOpacity onPress={() => onAdd(CartItem.product)}>
									<PlusCircle />
								</TouchableOpacity>

							</Actions>
						</Item>
					)}
				/>
			)}



			<Summary style={Platform.OS === "ios" ? {padding: 16} : {}}>
				<TotalContainer>

					{(isCartFilled) ? (
						<>
							<Text color="#666">Total</Text>
							<Text weight={600} size={20}>{formatCurrency(total)}</Text>
						</>
					) : (
						<Text color="#999">Seu carrinho está vazio</Text>

					)}


				</TotalContainer>

				{isCartFilled ? (
					<Button
						onPress={handleConfirmOrder}
						label="Confirmar pedido"
						loading={isLoading}
					>
					</Button>
				) : (
					<Button
						onPress={handleConfirmOrder}
						label="Confirmar pedido"
						disabled={true}
						loading={isLoading}
					>
					</Button>
				)}



			</Summary>

		</>
	)
}
