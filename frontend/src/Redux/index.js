import { combineReducers, configureStore } from "@reduxjs/toolkit";
import themeReducer from "./themeSlice";

const rootReducers = combineReducers({
    theme: themeReducer
})

const store = configureStore({
    reducer: rootReducers,
    devTools: false
})

export default store;