import path from 'node:path';

import { Router } from 'express';
import multer from 'multer';

import { listCategories } from './useCases/categories/listCategories';
import { createCategory } from './useCases/categories/createCategories';
import { listProducts } from './useCases/products/listProducts';
import { createProduct } from './useCases/products/createProducts';
import { listProductsByCategory } from './useCases/categories/listProductsByCategory';
import { listOrders } from './useCases/orders/listOrders';
import { createOrder } from './useCases/orders/createOrder';
import { changeOrderStatus } from './useCases/orders/changeOrderStatus';
import { cancelOrder } from './useCases/orders/cancelOrder';
import { deleteCategory } from './useCases/categories/deleteCateogories';
import { testFunc } from './useCases/test';



export const router = Router();

const upload = multer({
  storage: multer.diskStorage({

    destination(req, file, callback){
      callback(null,path.resolve(__dirname, '..', 'uploads'));
    },
    filename(req, file, callback) {
      callback(null, `${Date.now()}-${file.originalname}`); //timestamp - nome
    },
  })
});

router.get('/test', testFunc);

//List categories
router.get('/categories', listCategories);

//Create categories
router.post('/categories',createCategory);

//delete Categories
router.delete('/categories/:categoryId', deleteCategory);


//List products
router.get('/products', listProducts);

//Create product
router.post('/products', upload.single('image'), createProduct);

//Get products by category
router.get('/categories/:categoryId/products', listProductsByCategory);

//List orders
router.get('/orders', listOrders);

//Create order
router.post('/orders', createOrder);

//Change order status
router.patch('/orders/:orderId', changeOrderStatus);

//Delete/cancel order
router.delete('/orders/:orderId', cancelOrder);
