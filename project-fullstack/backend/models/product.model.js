import mongoose from "mongoose";

const productSchema = new mongoose.Schema({
    name: {
        type: String,
        requird: true
    },
    category: {
        type: String,
        enum: ["electronics"],
        default: "electronics"
    },
    organisationRef: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "Organisation"
    }
}, {timestamps: true});

export default mongoose.model("Product", productSchema);