---
layout: default
title: Brodalumab
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 10
---

# Brodalumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Brodalumab：從斑塊型乾癬到糞類圓線蟲症

## 一句話總結

Brodalumab 是一種 IL-17 受體 A（IL-17RA）拮抗劑，國際上已核准用於中重度斑塊型乾癬的治療。TxGNN 模型預測其排名第一的新適應症為**糞類圓線蟲症（Strongyloidiasis）**，預測分數高達 **99.84%**；然而，現有文獻顯示 IL-17 訊號對宿主抗蠕蟲防禦至關重要，阻斷 IL-17RA 可能**加重而非緩解**此感染，屬**反機轉（counter-indicated mechanism）預測**，目前無任何臨床試驗或文獻支持此再利用方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 中重度斑塊型乾癬（Moderate-to-severe plaque psoriasis） |
| 預測新適應症 | 糞類圓線蟲症（Strongyloidiasis） |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

目前 Evidence Pack 中**缺乏 Brodalumab 詳細的作用機轉資料**。根據公開資訊，Brodalumab 是一種全人源單株抗體，透過拮抗 IL-17 受體 A（IL-17RA），阻斷 IL-17A、IL-17F 及其他 IL-17 家族細胞激素的訊號傳遞，抑制下游促炎介質（如 IL-6、IL-8、G-CSF）的產生，進而緩解乾癬等慢性炎症性皮膚病的症狀。

TxGNN 知識圖譜模型可能透過疾病共病網路中的間接關聯，將 Brodalumab 與糞類圓線蟲症配對。然而，在機轉層面，**IL-17 訊號對宿主抗蠕蟲免疫防禦至關重要**——Th2/Th17 協同免疫反應是清除 *Strongyloides stercoralis* 感染的核心機制，IL-17 缺失會削弱腸道屏障完整性及嗜酸性球活化。

> ⚠️ **反機轉警示**：現有臨床文獻已記載 IL-17 抑制劑（secukinumab、ixekizumab）與**播散性糞類圓線蟲症**的相關風險案例。使用 IL-17 抑制劑被視為此感染症的**風險因子**而非治療選項。此 TxGNN 預測高分極可能源於疾病共病網路的遠端關聯，而非直接可治療機轉，**不建議作為再利用候選推進**。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **機轉層面的安全性提示**：根據 IL-17 生物學，Brodalumab 阻斷 IL-17RA 訊號軸可能削弱宿主對 *Strongyloides* 的清除能力，若用於免疫功能本已低下的患者（如長期使用類固醇者），有誘發播散性感染的潛在風險，與此再利用方向的安全性考量方向完全相悖。

---

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 預測分數雖達 99.84%，但機轉分析顯示此為**反機轉預測**：IL-17 訊號是宿主抵抗糞類圓線蟲症的關鍵防線，阻斷 IL-17RA 理論上會**惡化而非治療**此感染，與既有 IL-17 抑制劑的臨床安全性訊號一致。
- 證據等級 L5（無任何臨床前或臨床研究支持），決策門檻未達進入 S1 安全性評估的最低要求。

**若要推進需要：**
- 取得 Brodalumab 完整仿單，補充 MOA、警語及禁忌症資料（Data Gap DG001、DG002）
- 確認 TxGNN 此高分的網路拓撲來源（共病網路路徑溯源），釐清預測機制
- 重新評估是否存在 IL-17 訊號以外的替代治療靶點

> 💡 **建議優先轉向**：本報告排名第 2 的預測適應症**眼疾（Eye Disease，TxGNN 分數 99.82%）**具有較合理的機轉連結（IL-17A/F 在葡萄膜炎、鞏膜外層炎等眼部炎症中具文獻記載的促炎角色），並已有 1 個觀察性臨床試驗及 1 篇文獻支持，建議作為後續優先評估方向。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

