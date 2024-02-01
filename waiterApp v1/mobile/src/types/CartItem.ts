import { ProductType } from "./product"

export interface CartItem {
	product: ProductType;
	quantity: number;
}
