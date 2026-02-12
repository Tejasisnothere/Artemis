import mongoose from "mongoose";
import verifier from "verifier";

const userSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    organisation: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "Organisation"
    },
    email: {
        type: String,
        required: true,
        unique: true,
        // add verifier
    },
    password: {
        type: String,
        required: true,
    },
    role: {
        type: String,
        enum: ["admin", "manager", "viewer"];
        default: "admin"
    }
});

export default mongoose.model("User", userSchema);