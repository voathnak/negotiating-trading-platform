import {balanceConstants} from '../_constants';

export function balance(state = {}, action) {
  switch (action.type) {
    case balanceConstants.UPDATE_BALANCE:
      return {
        ...state,
        balance: action.balance
      };
    case balanceConstants.GET_ALL_BALANCE:
      return {
        ...state,
        balance: action.balance
      };
    default:
      return state
  }
}
