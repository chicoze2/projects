import { Request, Response} from 'express';

import { Category } from '../../models/Category';

export async function listCategories(req: Request, res: Response){
  try{
    const categories = await Category.find();
    res.json(categories);
  }catch (err){
    console.error(err);
    res.status(500).json({error: 'Error gathering category list info.'});
  }

}
