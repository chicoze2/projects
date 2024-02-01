import { Request, Response} from 'express';

import { io } from '../index';

const rota = 'order@new';
const payload = {
  'name': 'Second',
  'table': '12',
  'status': 'WAITING',
  'products': [
    {
      'product': {
        '_id': '123',
        'name': 'Esfiha',
        'description': 'Suculenta esfiha de carne tempeirada com ouro!',
        'imagePath': '1705510104774-esfiha.jpg',
        'price': 12,
        'ingredients': [],
        'category': '65a804d0a8b4bc20ebf2afbe',
        '__v': 0
      },
      'quantity': 1,
      '_id': '65ba5886d7ec670c2532b8a1'
    },
    {
      'product': {
        '_id': '6526bd8aa4047a43bbc5692e',
        'name': 'Coca Cola ',
        'description': 'Lata 350ml geladinha',
        'imagePath': '1697037706701-coca-cola.png',
        'price': 7,
        'ingredients': [],
        'category': '652604fd67ad8b4812e53ade',
        '__v': 0
      },
      'quantity': 2,
      '_id': '65ba5886d7ec670c2532b8a2'
    }
  ],
  '_id': 'ID123',
  'createdAt': '2024-01-31T14:26:14.418Z',
  '__v': 0
};


export function testFunc(req: Request, res: Response){

  console.log(`EMITINDO EM ${rota}`);
  io.emit(rota, payload);

  return res.status(200);

}
