---
layout: default
title: Trametinib
parent: 高證據等級 (L1-L2)
nav_order: 761
evidence_level: L2
indication_count: 5
---

# Trametinib
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Trametinib：從 BRAF V600 突變黑色素瘤到非皮膚型黑色素瘤

## 一句話總結

Trametinib（DB08911）是選擇性 MEK1/2 抑制劑，目前核准用於 BRAF V600E/K 突變之皮膚型黑色素瘤（多與 dabrafenib 併用）。TxGNN 模型預測它可能對**非皮膚型黑色素瘤（Non-cutaneous Melanoma）**——如黏膜、肢端、葡萄膜等亞型——同樣有效，目前有 **60+ 個相關臨床試驗**支持這個方向，但多數試驗設計仍以皮膚型 BRAF 突變族群為主，非皮膚亞型的專屬證據仍有限。

> 註：此藥物在 TxGNN 預測清單中共有 5 個候選適應症（choroideremia、non-cutaneous melanoma、epithelioid cell melanoma、eyelid melanoma、scrotum melanoma）。本報告聚焦於證據強度最高、最具行動性的第 2 名候選——非皮膚型黑色素瘤；其餘候選整理於文末附表。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 皮膚型 BRAF V600E/K 突變黑色素瘤（多與 dabrafenib 併用，正式適應症文字缺乏 HK 許可證資料佐證） |
| 預測新適應症 | 非皮膚型黑色素瘤 (Non-cutaneous Melanoma) |
| TxGNN 預測分數 | 99.30% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Trametinib 是選擇性 MEK1/2 抑制劑，透過阻斷 MAPK/ERK 訊號路徑抑制腫瘤細胞增生。目前已核准用於 BRAF V600E/K 突變陽性之皮膚型黑色素瘤，通常與 BRAF 抑制劑 dabrafenib 併用，以延緩單一抑制劑常見的抗藥性。

非皮膚型黑色素瘤（涵蓋黏膜、肢端、葡萄膜、結膜等亞型）與皮膚型黑色素瘤在組織起源上不同，但部分亞型（尤其是肢端型與結膜型）仍帶有 BRAF 突變，理論上可共享相同的 MAPK 路徑活化機轉。證據包中的臨床試驗如 NCT02083354 即明確納入「Acral lentiginous or cutaneous melanoma」病人群，顯示這個機轉延伸並非純粹推測。

需注意的是，非皮膚型亞型中 BRAF 突變盛行率明顯低於皮膚型（如葡萄膜黑色素瘤幾乎不帶 BRAF 突變，其驅動基因多為 GNAQ/GNA11），因此臨床應用上需要嚴格的分子分型篩選，不能直接外推整個「非皮膚型黑色素瘤」族群。

**作用機轉補充**：正式的 DrugBank MOA 欄位目前為資料缺口（DG002），以上機轉描述取自本次證據包之預測理由分析，建議後續正式查證 DrugBank API 以補齊完整機轉資料。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01941927](https://clinicaltrials.gov/study/NCT01941927) | Phase 2 | 完成 | 20 | Trametinib + GSK2141795（AKT抑制劑）用於 BRAF 野生型黑色素瘤，涵蓋非典型亞型族群 |
| [NCT01972347](https://clinicaltrials.gov/study/NCT01972347) | Phase 2 | 進行中 | 35 | Dabrafenib+trametinib 新輔助治療 Stage IIIB-C BRAF V600 突變黑色素瘤 |
| [NCT02910700](https://clinicaltrials.gov/study/NCT02910700) | Phase 2 | 進行中 | 52 | Nivolumab+trametinib+dabrafenib 三藥併用治療轉移性黑色素瘤 |
| [NCT03149029](https://clinicaltrials.gov/study/NCT03149029) | Phase 2 | 進行中 | 16 | 縮短療程 MAPK 標靶治療（含 trametinib）+ pembrolizumab |
| [NCT02083354](https://clinicaltrials.gov/study/NCT02083354) | Phase 2 | 完成 | 77 | Dabrafenib+trametinib 用於肢端（Acral）或皮膚型 BRAF V600 突變黑色素瘤，直接涵蓋非典型解剖部位亞型 |
| [NCT01584648](https://clinicaltrials.gov/study/NCT01584648) | Phase 3 | 完成 | 423 | 樞紐試驗：Dabrafenib+trametinib vs dabrafenib 單方治療一線 BRAF 突變黑色素瘤 |
| [NCT01245062](https://clinicaltrials.gov/study/NCT01245062) | Phase 3 | 完成 | 322 | Trametinib 單方 vs 化療（dacarbazine/paclitaxel）用於 BRAF V600E/K 突變黑色素瘤 |
| [NCT01597908](https://clinicaltrials.gov/study/NCT01597908) | Phase 3 | 完成 | 704 | Dabrafenib+trametinib vs vemurafenib 用於 BRAF V600E/K 突變黑色素瘤 |
| [NCT02039947](https://clinicaltrials.gov/study/NCT02039947) | Phase 2 | 完成 | 127 | Dabrafenib+trametinib 用於 BRAF 突變黑色素瘤腦轉移病人（非皮膚原發部位擴散情境） |
| [NCT01940809](https://clinicaltrials.gov/study/NCT01940809) | Phase 1 | 終止 | 15 | Ipilimumab±dabrafenib/trametinib/nivolumab，樣本小且提前終止 |

---

## 文獻證據

目前無「非皮膚型黑色素瘤」直接相關文獻。

> 補充：本證據包中相近的解剖亞型候選（結膜/眼瞼黑色素瘤、上皮樣細胞黑色素瘤，見文末附表）各有 2 篇個案報告／回顧文獻支持 BRAF/MEK 抑制劑於該類部位的反應性，可作為機轉延伸的間接佐證，詳見附表對應候選。

---

## 香港上市資訊

目前 Trametinib 在香港尚未取得任何藥品許可證（`market_status: 未上市`，`total_licenses: 0`），無許可證資料可列出。

---

## 細胞毒性

**Trametinib 為抗腫瘤標靶藥物（MEK1/2 抑制劑），適用本章節。**

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（MEK1/2 抑制劑），非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

（此藥目前查無 TFDA 仿單警語/禁忌資料，為 Blocking 等級資料缺口，見下方結論。）

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 其他 TxGNN 預測候選適應症（本評估包共 5 項）

| 排序 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|-----------|-----------|---------|---------|------|
| 1 | Choroideremia | 99.31% | L5 | S0 | Hold |
| **2** | **Non-cutaneous melanoma（本報告主題）** | **99.30%** | **L2** | **S3** | **Proceed with Guardrails** |
| 3 | Epithelioid cell melanoma | 99.28% | L4 | S1 | Research Question |
| 4 | Eyelid melanoma | 99.26% | L4 | S1 | Research Question |
| 5 | Scrotum melanoma | 99.21% | L5 | S0 | Hold |

Choroideremia（遺傳性視網膜退化疾病）與 scrotum melanoma（罕見部位黑色素瘤）雖 TxGNN 分數接近，但完全無臨床試驗或文獻支持，機轉上也缺乏與 MAPK/MEK 路徑的直接關聯，暫不建議推進。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 多個已完成的 Phase 2/3 試驗證實 trametinib（多與 dabrafenib 併用）在 BRAF V600 突變黑色素瘤中具療效，其中 NCT02083354 已涵蓋肢端型（Acral）等非典型皮膚亞型，機轉延伸至非皮膚型黑色素瘤具合理性。
- 但目前試驗證據仍以皮膚型 BRAF 突變族群為主體，非皮膚亞型（尤其葡萄膜型）的 BRAF 突變盛行率低，需嚴格分子分型篩選才能對應到真正受益族群。

**若要推進需要：**
- **補齊 TFDA 仿單警語與禁忌資料**（DG001，Blocking 等級，目前無法完成 S1 安全性初評）
- **查詢 DrugBank API 補齊正式 MOA 紀錄**（DG002）
- 香港目前未上市，需評估藥證申請路徑或透過恩慈療法／專案進口機制
- 針對非皮膚型黑色素瘤各亞型（黏膜、肢端、葡萄膜）分別確認 BRAF 突變盛行率與現有臨床反應資料，避免以皮膚型試驗結果一概外推
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

