import React from "react"
import { Text } from "../Text"
import { Container } from "./styles"
import { ActivityIndicator } from "react-native";

interface ButtonProps {

	label: string;
	disabled?: boolean;
	loading?: boolean;

	onPress: () => void;

}

export function Button({label, onPress, disabled, loading}: ButtonProps) {
	return (
		<Container onPress={onPress} disabled={disabled || loading }>
			{!loading && (
				<Text weight="600" color="#fff">{label}</Text>
			)}

			{loading && (
				<ActivityIndicator color='#fff' />
			)}

		</Container>
	)
}
