const express = require('express');
const path = require('path');
const fetch = require('node-fetch');

const app = express();
const PORT = 3000;

// Serve static files
app.use(express.static(__dirname));
app.use(express.json());

// MiniMax API proxy
app.post('/api/ai-analyze', async (req, res) => {
    const { stockCode, stockName, query } = req.body;
    const apiKey = process.env.MINIMAX_API_KEY;
    
    if (!apiKey) {
        return res.status(500).json({ error: 'No API key configured' });
    }

    const systemPrompt = `你是一个专业的香港IPO分析师，名为"IPO小助手"。你的职责是：
1. 分析新股的热度和投资价值
2. 提供认购建议和风险提示
3. 用简洁专业的中文回复
4. 回复格式要清晰，用bullet points列表
5. 每次回复不要太长，控制在200字以内`;

    const userPrompt = query || `分析${stockName}(股票代码:${stockCode})的新股认购价值，包括：
- 行业热度
- 集资规模
- 暗盘/上市表现预测
- 认购建议
- 风险提示`;

    try {
        const response = await fetch('https://api.minimax.chat/v1/text/chatcompletion_pro?GroupId=your_group_id', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                model: 'abab6-chat',
                tokens_to_generate: 512,
                temperature: 0.7,
                top_p: 0.95,
                messages: [
                    { role: 'system', content: systemPrompt },
                    { role: 'user', content: userPrompt }
                ]
            })
        });

        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }

        const data = await response.json();
        const reply = data.choices?.[0]?.text || '抱歉，AI 分析暂时不可用';
        
        res.json({ success: true, analysis: reply });
    } catch (error) {
        console.error('MiniMax API error:', error);
        res.status(500).json({ error: error.message });
    }
});

app.listen(PORT, () => {
    console.log(`🎮 IPO Tracker running at http://localhost:${PORT}`);
});
