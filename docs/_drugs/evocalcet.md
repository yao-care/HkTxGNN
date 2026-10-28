---
layout: default
title: Evocalcet
parent: 僅模型預測 (L5)
nav_order: 358
evidence_level: L5
indication_count: 8
monitor_inn: "EVOCALCET"
predicted_indications: ["hyperphosphatemia (disease)", "tumoral calcinosis, hyperphosphatemic, familial", "familial hyperphosphatemic tumoral calcinosis/hyperphosphatemic hyperostosis syndrome", "pancreatitis", "hereditary hypercarotenemia and vitamin A deficiency", "primary hyperoxaluria", "familial apolipoprotein C-II deficiency", "C1 inhibitor deficiency"]
last_modified_at: 2026-10-23
description: "Evocalcet：預測新適應症為高磷血症 (Hyperphosphatemia)（證據等級 L5）。原適應症：副甲狀腺機能亢進"
---

# Evocalcet
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Evocalcet：從副甲狀腺機能亢進到高磷血症
{: .text-alpha }

## 一句話總結

Evocalcet 是一種鈣敏感受體（CaSR）調節劑（擬鈣劑），知識圖譜中記錄的原適應症為副甲狀腺機能亢進。
TxGNN 模型預測它可能對**高磷血症 (Hyperphosphatemia)** 有效，
但目前**沒有臨床試驗**，僅有 **2 篇文獻**（1 篇前臨床研究、1 篇與主題關聯有限的病例報告），且都未直接研究此疾病，證據仍屬模型預測層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 副甲狀腺機能亢進（知識圖譜記錄的關係；香港許可證未載明適應症文字） |
| 預測新適應症 | 高磷血症 (Hyperphosphatemia) |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏經正式資料庫確認的詳細作用機轉資料。根據藥理資料，Evocalcet 是變構型擬鈣劑，作用於副甲狀腺細胞上的鈣敏感受體（CASR），抑制副甲狀腺素（PTH）分泌。

PTH 下降可減少骨吸收及鈣、磷的釋放，因此血磷理論上可能間接下降。前臨床研究（PMID 29614098）描述了 Evocalcet 抑制副甲狀腺細胞功能，且對腸胃道影響較小。不過，這只是慢性腎臟病繼發性副甲狀腺機能亢進情境下可能的次要效應，**並非直接降磷療效的證據**。

此外，此預測的證據中，沒有任何一項研究直接以高磷血症為對象，因此依規則證據等級只能判定為 L5。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29614098](https://pubmed.ncbi.nlm.nih.gov/29614098/) | 2018 | 前臨床研究 | PloS one | 新型擬鈣劑 Evocalcet 可抑制副甲狀腺細胞功能，對腸胃道及 CYP 酵素影響小 |
| [40471524](https://pubmed.ncbi.nlm.nih.gov/40471524/) | 2025 | 病例報告 | Clinical journal of gastroenterology | 先天性肝纖維化合併繼發性副甲狀腺機能亢進患者出現快速進展的瀰漫性肝鈣化；不足以證實療效 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68425 | ORKEDIA TABLETS 2MG | 錠劑 | 未提供 |
| HK-68424 | ORKEDIA TABLETS 1MG | 錠劑 | 未提供 |

## 安全性考量

- **藥物交互作用**：藥理資料僅顯示其作用標的為 CASR（鈣敏感受體），未列出具體藥物間交互作用。

其餘安全性資訊（警語、禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 高磷血症預測僅有模型分數與間接的機轉推論，沒有臨床試驗，也沒有直接研究此疾病的文獻。
- 擬鈣劑透過降低 PTH 對血磷的影響是間接的，尚未有 Evocalcet 直接降磷的證據。

**若要推進需要：**
- 取得 Evocalcet 在透析或慢性腎臟病患者血磷變化的臨床資料（如既有繼發性副甲狀腺機能亢進試驗的血磷次要指標）。
- 補充作用機轉資料及香港仿單的警語、禁忌症與核准適應症。
- 評估是否需要設計以血磷為主要終點的前瞻性研究。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

