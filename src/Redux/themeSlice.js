import { createSlice } from "@reduxjs/toolkit"

const initialState = {
    themeMode: "dark"
}

const themeSlice = createSlice({
    name: "theme",
    initialState: initialState,
    reducers: {
        changeTheme(state, action) {
            if (state.themeMode === "light") {
                state.themeMode = "dark";
            } else {
                state.themeMode = "light";
            }
        }
    },
    // extraReducers(builder){
    //     builder
    //         .addCase(fatchData.)
    // }
})

export const themeMode = state => (state.theme.themeMode)
export const { changeTheme } = themeSlice.actions;

export default themeSlice.reducer;