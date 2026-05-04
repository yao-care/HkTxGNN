---
layout: default
title: Alfentanil
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 1
---

# Alfentanil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# ALFENTANIL：從術中鎮痛到腎源性抗利尿不當症候群

## 一句話總結

Alfentanil 是一種短效 μ-opioid 受體促效劑，原本用於**術中鎮痛與麻醉誘導**。
TxGNN 模型預測它可能對**腎源性抗利尿不當症候群（Nephrogenic Syndrome of Inappropriate Antidiuresis，NSIAD）** 有效，
然而目前**無任何臨床試驗或文獻**支持此方向，且機轉分析顯示此預測存在反向作用疑慮。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 術中鎮痛 / 麻醉誘導（短效 opioid） |
| 預測新適應症 | 腎源性抗利尿不當症候群（Nephrogenic Syndrome of Inappropriate Antidiuresis） |
| TxGNN 預測分數 | 99.51% |
| 證據等級 | L5 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

> 目前缺乏詳細的作用機轉資料。根據已知資訊，Alfentanil 是短效 μ-opioid 受體促效劑，主要用於術中鎮痛與麻醉，其在鎮痛領域的療效已被充分驗證。

**然而，此預測的機轉合理性存在根本性問題。**

NSIAD（腎源性抗利尿不當症候群）由 *AVPR2* 基因功能增益突變引起，導致 V2 vasopressin 受體在缺乏 ADH 刺激的情況下持續活化，臨床上表現為難治性低鈉血症。

從藥理機轉角度看，μ-opioid 激活已知可**促進** ADH 分泌，此效應在正常個體可能誘發 SIADH，若套用於已有 V2 受體過度活化的 NSIAD 患者，理論上會**加重病情**而非改善。因此，目前**無合理的藥理假說**支持 alfentanil 可治療 NSIAD。

TxGNN 的高分（0.995，排名第 8,831）推測源自知識圖譜的**拓樸相似性推斷**：opioid → ADH 系統 → 水分平衡 → 低鈉血症 → NSIAD，屬間接路徑連結，並不代表真實的治療關聯。此類「圖譜捷徑」是 GNN 模型的已知局限性之一。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

Alfentanil 在台灣**未曾取得藥品許可證**，目前未上市流通。若需在台灣使用，需透過專案進口或特殊管道申請。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉分析顯示 alfentanil 的 opioid 藥理效應可能**加重** NSIAD 病情，而非改善，缺乏正向治療假說。
- 目前完全缺乏臨床試驗與文獻支持（L5 等級），且 TxGNN 高分源自間接拓樸推斷，不具備直接生物學依據。

**若仍希望評估此方向，需先完成：**
- [ ] 確認 alfentanil 對 AVPR2 功能增益突變細胞模型的體外效應（反向機轉風險排除）
- [ ] 搜尋 opioid 類藥物與 V2 receptor 交互作用的前臨床文獻
- [ ] 釐清 TxGNN 模型的圖譜路徑細節，評估是否存在其他間接治療假說
- [ ] 補充 TFDA 仿單安全性資料（DG001）及 DrugBank MOA 資料（DG002）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

