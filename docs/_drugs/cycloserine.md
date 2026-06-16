---
layout: default
title: Cycloserine
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 7
---

# Cycloserine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cycloserine：從結核病到腸躁症

## 一句話總結

Cycloserine 是一種二線廣譜抗生素，主要用於耐多藥結核病（MDR-TB）的治療。
TxGNN 模型預測它可能對**腸躁症 (Irritable Bowel Syndrome)** 有效，
然而目前**無任何臨床試驗登記**，亦**無相關文獻**支持此方向，屬純模型預測（L5 等級）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 耐多藥結核病（MDR-TB） |
| 預測新適應症 | 腸躁症 (Irritable Bowel Syndrome) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Cycloserine 是細菌細胞壁合成抑制劑，透過競爭性拮抗 D-丙胺酸（D-alanine）的代謝途徑發揮抗菌作用；D-Cycloserine 的立體異構體同時具有 NMDA 受體部分激動活性。

對於腸躁症，目前有兩條間接推測路徑：
1. **腸道菌叢路徑**：Cycloserine 的廣譜抗菌活性可能改變腸道菌叢組成，而腸道菌叢失調被視為腸躁症的潛在致病因素之一。
2. **腸腦軸路徑**：D-Cycloserine 作為 NMDA 受體部分激動劑，理論上可透過腸腦軸（gut-brain axis）調節腸道運動功能。

然而，上述兩條路徑均屬間接假說，目前完全無動物模型或人體試驗數據支持 Cycloserine 用於腸躁症。此預測很可能反映的是知識圖譜中藥物-疾病的間接網絡關聯，而非真實的治療潛力。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Cycloserine 目前在香港**未登記上市**，無任何許可證紀錄。如需使用，須透過特殊管道申請。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **安全警示**：雖然正式安全性資料尚待補充，但根據本次評估中其他適應症的文獻紀錄（PMID [36712725](https://pubmed.ncbi.nlm.nih.gov/36712725/)），Cycloserine 在 MDR-TB 治療過程中已明確記錄可**誘發失眠及精神病症狀**（CNS 毒性）。此藥物的神經毒性風險在評估任何新適應症時均需優先考量。

---

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 雖給出 99.95% 的高預測分數，但腸躁症目前屬 L5 純模型預測，完全缺乏臨床試驗及文獻支持，且機轉連結為間接推測。
- Cycloserine 已知具有顯著的中樞神經系統毒性（失眠、精神症狀），在無有效性證據的情況下，其風險效益比完全不支持推進腸躁症的再利用研究。

**若要推進需要：**
- 完整的作用機轉資料（MOA），特別是 NMDA 受體與腸道神經系統的關聯
- 腸躁症動物模型的前臨床研究數據
- 腸道菌叢與 Cycloserine 交互作用的機轉研究
- 完整安全性資料（TFDA 仿單警語、禁忌症）以通過 S1 安全性初評
- 香港藥監當局特殊使用申請評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

