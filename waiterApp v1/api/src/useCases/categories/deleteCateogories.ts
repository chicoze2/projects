import { Category } from '../../models/Category';
import { Request, Response} from 'express';


export async function deleteCategory(req: Request, res: Response){

  const {categoryId} = req.params;
  const category = await Category.findByIdAndRemove(categoryId);

  return res.send(category);

}
