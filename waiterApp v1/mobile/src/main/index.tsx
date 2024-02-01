import axios from "axios"
import { api } from "../utils/api"

import React = require("react")
import { useEffect, useState } from "react"
import { ActivityIndicator } from "react-native"


import {
	Container,
	CategoriesContainer,
	Footer,
	MenuContainer,
	FooterContainer,
	ContainerButtonIOS,
	CenteredContainer

} from "./styles"

import { Header } from "../components/Header"
import { Categories } from "../components/Categories"
import { Menu } from "../components/Menu"
import { Button } from "../components/Button"
import { TableModal } from "../components/TableModal"
import { Empty } from "../components/Icons/Empty"
import { Cart } from "../components/Cart"
import { CartItem } from "../types/CartItem"
import { Text } from "../components/Text"

import { products  as mockProducts} from "../mocks/products"
// eslint-disable-next-line @typescript-eslint/no-unused-vars
import { categories as mockCategories } from "../mocks/categories"

import { ProductType } from "../types/product"
import { Category } from "../types/Category"


export function Main() {

	const [isTableModalVisible, setIsTableModalVisible] = useState(false)
	const [selectedTable, setSelectedTable] = useState("")
	const [cartItens, setCartItens] = useState<CartItem[]>([])
	const [isLoading, setIsLoading] = useState(true)
	const [products, setProducts] = useState<ProductType[]>([])
	const [categories, setCategories] = useState<Category[]>([])
	const [isLoadingProducts, setIsLoadingProducts] = useState(false)

	useEffect(() => {

		Promise.all([
			api.get("/categories"),
			api.get("/products"),
		]).then(([categoriesResponse, productsResponse]) => {
			setProducts(productsResponse.data)
			setCategories(categoriesResponse.data)
			setIsLoading(false)
		})
	}, [])


	async function handleSelectCategory(categoryId: string) {

		const route = !categoryId
			? "/products"
			: `/categories/${categoryId}/products`

		setIsLoadingProducts(true)

		const { data } = await api.get(route)
		setProducts(data)

		setIsLoadingProducts(false)
	}

	function handleSaveTable(table: string) {
		setSelectedTable(table)
		setIsTableModalVisible(false)
	}

	function  handleFinishOrder() {
		setSelectedTable("")
		setCartItens([])
	}


	function handleAddToCart(product: ProductType) {
		if(!selectedTable){
			setIsTableModalVisible(true)
		}

		setCartItens((prevState) => {
			const itemIndex = prevState.findIndex(
				cartItens => cartItens.product._id === product._id
			)

			if(itemIndex < 0){
				return prevState.concat({
					quantity: 1,
					product
				})
			}

			const newCartItens = [...prevState]
			newCartItens[itemIndex] = {
				...newCartItens[itemIndex],
				quantity: newCartItens[itemIndex].quantity + 1
			}

			return newCartItens


		})
	}

	function handleDecrementCartItem(product: ProductType) {
		setCartItens((prevState) => {
			const itemIndex = prevState.findIndex(
				cartItens => cartItens.product._id === product._id
			)

			const item = prevState[itemIndex]
			const newCartItens = [...prevState]

			if(item.quantity === 1){//CASO SEJA ULTIMO ITEM (QTDx1) -> splice(remove do array) =! qtd ==0
				newCartItens.splice(itemIndex, 1)
				return newCartItens

			}else{

				newCartItens[itemIndex] = {
					...item,
					quantity: item.quantity - 1
				}
				return newCartItens

			}


		})
	}

	return (
		<>
			<Container>

				<Header
					selectedTable={selectedTable}
					onCancelOrder={handleFinishOrder}
				/>

				{!isLoading && (

					<>
						<CategoriesContainer>
							<Categories
								categories={categories}
								onSelectCategory={handleSelectCategory}/>
						</CategoriesContainer>

						{isLoadingProducts ? (
							<CenteredContainer>
								<ActivityIndicator color="#D73035" size="large"/>
							</CenteredContainer>
						) : (
							<>
								{products.length > 0 ? (
									<MenuContainer>
										<Menu
											onAddToCart={handleAddToCart}
											products={products}/>
									</MenuContainer>
								) : (
									<CenteredContainer>
										<Empty />
										<Text color="#666" style={{marginTop: 24}}>Nenhum produto foi encontrado </Text>
									</CenteredContainer>
								)}
							</>
						)}



					</>

				)}

				{isLoading && (
					<CenteredContainer>
						<ActivityIndicator color="#D73035" size="large"/>
					</CenteredContainer>
				)}

			</Container>

			<Footer>
				<FooterContainer>
					{!selectedTable && (

						<ContainerButtonIOS>
							<Button
								disabled={selectedTable.length < 0 || isLoading}
								onPress={() => setIsTableModalVisible(true)}
								label='Novo Pedido'/>
						</ContainerButtonIOS>


					)}

					{(selectedTable) && (
						<Cart
							cartItems={cartItens}
							onAdd={handleAddToCart}
							onRemove={handleDecrementCartItem}
							onConfirmOrder={handleFinishOrder}
							selectedTable={selectedTable}
						></Cart>
					)}

				</FooterContainer>
			</Footer>

			<TableModal
				visible={isTableModalVisible}
				onClose={ () => setIsTableModalVisible(false)}
				onSave={handleSaveTable}

			/>

		</>
	)
}

