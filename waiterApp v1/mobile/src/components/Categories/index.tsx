import { FlatList } from "react-native"

import React, { useState } from "react"
import { Text } from "../Text"

import { Category, Icon } from "./styles"
import { Category as CategoryType } from "../../types/Category"

interface CategoriesProps {
	categories: CategoryType[]
	onSelectCategory: (categoryId: string) => Promise<void>
}

export function Categories({categories, onSelectCategory}: CategoriesProps) {

	const [selectedCategory, setSelectedCategory] = useState("")

	function handleSelectCategory(categoryId: string) {

		const category = selectedCategory === categoryId ? "" : categoryId

		setSelectedCategory(category)
		onSelectCategory(category)
	}


	return (

		<FlatList
			horizontal /* (true) */
			contentContainerStyle={{paddingRight: 24}}
			showsHorizontalScrollIndicator={false}
			data={categories}
			keyExtractor={(category) => category._id}
			renderItem={({ item: category }) => {


				const isSelected = selectedCategory == category._id

				return(
					<Category onPress={() => handleSelectCategory(category._id)}>
						<Icon>
							<Text opacity={isSelected ? 1 : 0.5}>{category.icon}</Text>
						</Icon>

						<Text size={14} weight="600" opacity={isSelected ? 1 : 0.5}>
							{category.name}
						</Text>
					</Category>
				)
			}}
		/>

	)
}
