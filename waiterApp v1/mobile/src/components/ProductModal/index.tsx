import React from "react"
import { FlatList, Modal } from "react-native"

import { Text } from "../Text"
import { Image, CloseButton, ModalBody, Header, IngredientsContainer, Ingredient, FooterContainer, Footer, PriceContainer} from "./styles"
import { ProductType } from "../../types/product"
import { Close } from "../Icons/Close"
import { formatCurrency } from "../../utils/formatCurrency"
import { Button } from "../Button"

interface ProductModalProps {
	visible: boolean;
	product: ProductType | null;
	onClose: () => void;
	onAddToCart: (product : ProductType) => void;

}

export function ProductModal({ visible, product, onClose, onAddToCart } : ProductModalProps ) {

	if(!product){
		return null
	}

	function handleAddToCart(product : ProductType){
		onAddToCart(product!)
		onClose()
	}

	return(

		<Modal
			visible={visible}
			animationType="slide"
			presentationStyle="pageSheet"
			onRequestClose={onClose}
		>

			<Image
				source={{
					uri: `http://192.168.1.100:3000/uploads/${product.imagePath}`

				}}
			>

				<CloseButton onPress={onClose}>
					<Close />
				</CloseButton>

			</Image>

			<ModalBody>
				<Header>
					<Text size={24} weight="600" >{product.name}</Text>
					<Text color="#666" style={{marginTop: 8}}>{product.description}</Text>
				</Header>

				{product.ingredients.length > 0 && (
					<IngredientsContainer>
						<Text color="#666" weight="600">Ingredientes</Text>

						<FlatList
							data={product.ingredients}
							keyExtractor={ingredient => ingredient._id}
							showsVerticalScrollIndicator={false}

							style={{marginTop: 16}}

							renderItem={({item: ingredient}) => (
								<Ingredient>
									<Text>{ingredient.icon}</Text>
									<Text color="#666" size={16} style={{marginLeft: 20}}> {ingredient.name}</Text>
								</Ingredient>
							)}
						/>

					</IngredientsContainer>

				)}


			</ModalBody>

			<Footer>
				<FooterContainer>
					<PriceContainer>
						<Text color='#666'>Preço</Text>
						<Text size={20} weight="600">{formatCurrency(product.price)}</Text>
					</PriceContainer>

					<Button label="Adicionar ao pedido" onPress={() => handleAddToCart(product)}> </Button>

				</FooterContainer>
			</Footer>

		</Modal>
	)

}
