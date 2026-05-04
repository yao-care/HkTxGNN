---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 3
---

# Empagliflozin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Empagliflozin：從第二型糖尿病到僵硬人症候群

## 一句話總結

Empagliflozin 是一種 SGLT2 抑制劑，廣泛用於第二型糖尿病及心臟衰竭的治療。TxGNN 模型預測它可能對**僵硬人症候群 (Classic Stiff Person Syndrome)** 有效，機轉假說以免疫調節效應為基礎。目前**無任何臨床試驗或文獻**支持此方向，屬純模型預測階段，建議暫緩推進。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 原始資料缺乏（已知為 SGLT2 抑制劑，用於第二型糖尿病） |
| 預測新適應症 | 僵硬人症候群 (Classic Stiff Person Syndrome) |
| TxGNN 預測分數 | 99.06% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Empagliflozin 是 SGLT2（鈉-葡萄糖共同轉運蛋白 2）抑制劑，主要透過抑制腎臟葡萄糖再吸收以降低血糖，並在代謝層面具有廣泛的下游效應，包括心臟與腎臟保護作用。

針對僵硬人症候群（SPS）的機轉假說，來自 SGLT2 抑制劑已知的抗炎與免疫調節特性：(1) 抑制 NF-κB 信號途徑，減少 IL-6、TNF-α 等促炎細胞因子；(2) 通過 AMPK-mTOR 軸調節 T 細胞活化；(3) 降低氧化壓力（減少 ROS 生成）。SPS 是一種由自身抗體（主要是抗 GAD65 抗體）驅動的自身免疫性疾病，理論上抗炎效應可能帶來一定益處。

然而，這條機轉連結具有高度間接性。SGLT2 在中樞神經系統（CNS）的表達量極低，藥物穿透血腦屏障的能力有限，且完全缺乏直接針對 GABAergic 神經系統的作用靶點。整體機轉可信度評估為**極低**，此預測主要反映知識圖譜中的拓撲關聯性，而非具體的生物機轉依據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

> 查詢範圍涵蓋 ClinicalTrials.gov 及 ICTRP，查詢日期：2026-03-25，三個預測適應症均無結果。

---

## 文獻證據

目前無相關文獻。

> 查詢範圍涵蓋 PubMed，查詢日期：2026-03-25，三個預測適應症均無結果。

---

## 香港上市資訊

Empagliflozin 目前在香港**尚未取得上市許可**，無任何藥品許可證登記記錄。

---

## 預測適應症補充分析

本報告同時收錄排名第 2、3 的預測結果，供完整評估參考：

| 排名 | 疾病名稱 | TxGNN 分數 | 知識圖譜排名 | 機轉可信度 | 建議 |
|------|---------|-----------|------------|----------|------|
| 1 | Classic Stiff Person Syndrome | 99.06% | #14,723 | 極低 | Hold |
| 2 | Focal Stiff Limb Syndrome | 99.06% | #14,724 | 極低 | Hold |
| 3 | Opsismodysplasia | 99.03% | #15,126 | 極低（方向可能相反）| Hold |

**Focal Stiff Limb Syndrome（局部僵硬肢體症候群）**：機轉假說與 Classic SPS 完全相同。需注意兩者的 TxGNN 分數完全一致（0.9906036257743835），反映在知識圖譜中的結構相似性，而非獨立的疾病特異性預測。Focal SPS 疾病異質性更高，部分病例與腫瘤旁症候群相關，免疫機轉更為複雜。

**Opsismodysplasia（骨幹增生不良症）**：理論連結路徑為 SGLT2 抑制劑 → AMPK 活化 → mTOR/PI3K 信號調節 → SHIP2（INPPL1 產物）途徑。然而，SHIP2 功能喪失導致 PI3K 過度活化，而 SGLT2 抑制劑介入的方向與治療需求的對應關係**不明確甚至可能相反**。此外，SGLT2 抑制劑對骨代謝的影響在部分研究中顯示可能**增加骨折風險**，對遺傳性骨骼發育疾病可能有害而非有益，不建議推進此方向。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
三個預測適應症均無任何臨床試驗或文獻支持（L5 純模型預測），機轉連結高度間接且可信度極低；其中 Opsismodysplasia 的機轉方向甚至可能對疾病有害。Empagliflozin 在香港尚未取得上市許可，缺乏在地監管基礎，若要開展臨床研究需經完整的新藥臨床試驗審查流程。

**若要推進需要：**
- 補充 Empagliflozin 詳細作用機轉資料（MOA）及當前已核准適應症清單
- 補充仿單警語與禁忌症資料，完成 S1 安全性初評（目前為 Blocking 缺口）
- 進行系統性文獻搜索，確認 SGLT2 抑制劑與自身免疫神經疾病（SPS）的基礎科學或動物模型證據
- 評估香港法規路徑（未上市藥物需考慮臨床試驗申請流程）
- **Opsismodysplasia 建議不予推進**（機轉方向可能有害，應從候選清單中移除）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

