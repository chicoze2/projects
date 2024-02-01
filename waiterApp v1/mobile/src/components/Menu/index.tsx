import React, {useState} from "react"
import { FlatList} from "react-native"

import { ProductType } from "../../../src/types/product"
import { Text} from "../Text"
import { formatCurrency } from "../../utils/formatCurrency"
//Componentes do Menu:
import { Product, ProductImage, ProductDetails, Spacer, AddToCartButton} from "./styles"
import { PlusCircle } from "../Icons/PlusCircle"
import { ProductModal } from "../ProductModal"

interface MenuProps {
	onAddToCart: (product: ProductType) => void;
	products?: Array<ProductType> | null;
}

export function Menu({onAddToCart, products} : MenuProps){

	const [isModalVisible, setIsModalVisible] = useState(false)
	const [selectedProduct, setSelectedProduct] = useState<null | ProductType>(null)

	function handleOpenProductModal(product : ProductType) {
		setIsModalVisible(true)
		setSelectedProduct(product)
	}

	return (
		<>

			<ProductModal
				visible={isModalVisible}
				product={selectedProduct}
				onClose={() => setIsModalVisible(false)}
				onAddToCart={onAddToCart}
			>

			</ProductModal>

			<FlatList
				data={products}

				style={{marginTop: 32}}
				contentContainerStyle={{ paddingHorizontal: 24 }}

				ItemSeparatorComponent={Spacer}

				keyExtractor={product => product._id}
				renderItem={({item: product}) => (
					<Product onPress={() => handleOpenProductModal(product)}>
						<ProductImage
							source={{
								uri: `http://192.168.1.100:3000/uploads/${product.imagePath}`

							}}

						/>

						<ProductDetails>

							<Text weight='600'>{product.name}</Text>
							<Text size={14} color="#666" style={{ marginVertical: 8 }}> {product.description}</Text>
							<Text size={14} weight='600'>{formatCurrency(product.price)}</Text>

						</ProductDetails>

						<AddToCartButton onPress={() => onAddToCart(product)}>
							<PlusCircle />
						</AddToCartButton>

					</Product>
				)}>

			</FlatList>
		</>
	)

}


