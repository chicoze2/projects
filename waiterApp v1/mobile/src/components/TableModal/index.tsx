import React, {useState} from "react"
import { Modal, TouchableOpacity, Platform } from "react-native"

import { Text } from "../Text"
import { Button } from "../Button"

import { ModalBody, ModalForm, ModalHeader, Overlay, Input } from "./styles"
import { Close } from "../Icons/Close"


interface TableModalProps {
	visible: boolean;
	onClose: () => void;
	onSave: (table: string) => void;
}



export function TableModal({ visible, onClose, onSave } :TableModalProps) {

	const [table, setTable] = useState("")

	return (
		<Modal
			transparent
			visible={visible}
			animationType="fade"
		>

			<Overlay behavior= { Platform.OS == "android" ? "height" : "padding"}>
				<ModalBody>

					<ModalHeader>
						<Text weight='600'> Informe a mesa</Text>

						<TouchableOpacity onPress={() => {onClose(); setTable("")}}>
							<Close color='#666'/>
						</TouchableOpacity>
					</ModalHeader>

					<ModalForm>

						<Input
							placeholder="Numero da mesa"
							placeholderTextColor="#666"
							keyboardType="number-pad"
							onChangeText={value => setTable(value)}
						/>

						<Button
							label="Salvar"
							onPress={() => {onSave(table); setTable("")}}
							disabled={table.length === 0}
						/>

					</ModalForm>

				</ModalBody>
			</Overlay>

		</Modal>
	)
}
