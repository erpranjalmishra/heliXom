// server.js
const express = require('express');
const { OAuth2Client } = require('google-auth-library');
const app = express();
const client = new OAuth2Client('555647419945-rnhflm67o76v48jcj8a04it7g0e10nfh.apps.googleusercontent.com');

app.use(express.json());

app.post('/auth/google', async (req, res) => {
    const token = req.body.token;

    try {
        const ticket = await client.verifyIdToken({
            idToken: token,
            audience: '555647419945-rnhflm67o76v48jcj8a04it7g0e10nfh.apps.googleusercontent.com',
        });

        const payload = ticket.getPayload();
        const userid = payload['sub'];

        res.status(200).json({ success: true, user: payload });
    } catch (error) {
        console.error("Error verifying token:", error);
        res.status(400).json({ success: false, error: 'Invalid token' });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
