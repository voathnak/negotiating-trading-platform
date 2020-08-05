import { balanceService } from "../_services";
const { balanceConstants } = require("../_constants");

export const balanceActions = {
    updateBalance,
    getAllBalance
};

function updateBalance (newBalance) {
    return dispatch => {
        balanceService.updateAll(newBalance)
          .then(
            balance => dispatch({type: balanceConstants.GET_ALL_BALANCE, balance})
          )
    }
}

function getAllBalance () {
    return dispatch => {
        // dispatch({type: balanceConstants.GET_ALL_BALANCE, balance})
        balanceService.getAll()
        .then( balance => dispatch({type: balanceConstants.GET_ALL_BALANCE, balance}))
    }
}

function rawGetAllBalance () {
        return balanceService.getAll()
          .then(response => response.text())
          .then(result => console.log(result))
          .catch(error => console.log('error', error));
}
