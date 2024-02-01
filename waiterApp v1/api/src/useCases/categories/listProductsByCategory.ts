import { Request, Response} from 'express';

import { Product } from '../../models/Product';

export async function listProductsByCategory(req: Request, res: Response){

  try{
    const product = await Product.find().where('category').equals(req.params.categoryId);
    res.send(product);

  }catch (err){
    console.error(err);
    res.status(500).json({error: 'Error gathering product info.'});
  }


}
