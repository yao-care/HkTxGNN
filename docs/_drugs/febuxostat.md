---
layout: default
title: Febuxostat
parent: 中證據等級 (L3-L4)
nav_order: 307
evidence_level: L3
indication_count: 3
---

# Febuxostat
{: .fs-9 }

證據等級: **L3** | 預測適應症: **3** 個
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

# Febuxostat：從痛風高尿酸血症到腎性低尿酸血症

## 一句話總結

Febuxostat 是非嘌呤類選擇性黃嘌呤氧化還原酶（XOR）抑制劑，原本在全球多個市場核准用於治療痛風患者的慢性高尿酸血症。
TxGNN 模型預測它可能對**腎性低尿酸血症（Hypouricemia, Renal）**有效，
目前有 **1 個臨床試驗**和 **2 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 痛風合併慢性高尿酸血症（全球核准適應症；香港本地許可證無登記） |
| 預測新適應症 | 腎性低尿酸血症（Hypouricemia, Renal） |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏正式的作用機轉文件（Data Gap DG002）。根據藥理學已知資訊，Febuxostat 透過選擇性、非競爭性地抑制黃嘌呤氧化還原酶（XOR），同步阻斷次黃嘌呤→黃嘌呤→尿酸的代謝路徑，進而大幅降低血清與尿液中的尿酸濃度及其前驅嘌呤負荷。

乍看之下，將「降尿酸藥」用於尿酸已偏低的腎性低尿酸血症（RHUC）似乎矛盾。關鍵在於 RHUC 最危險的合併症——**運動誘發性急性腎損傷（EIAKI）**。RHUC 患者因尿酸轉運子（URAT1 或 GLUT9）缺陷，腎臟無法重吸收尿酸，導致大量黃嘌呤與次黃嘌呤滯留腎小管。劇烈運動時，這些嘌呤代謝物在腎小管急速堆積，誘發氧化壓力與腎小管損傷。Febuxostat 透過抑制 XOR，從上游減少腎小管中黃嘌呤與次黃嘌呤的產量，理論上可預防 EIAKI 反覆發作。

PMID 36754409 報告了一例 16 歲日本足球運動員，患有家族性 RHUC（URAT1 複合雜合突變）且反覆 EIAKI，在標準補水預防失敗後，嘗試 Febuxostat 作為預防性治療的案例，為此機轉提供了直接的臨床觀察依據。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | 未知 | 100 | 上海徐匯中心醫院泌尿科前瞻性對照研究，探討尿酸控制對**高尿酸血症**結石患者之結石復發率與腎功能的影響（注意：為高尿酸血症族群，非直接針對 RHUC） |

> ⚠️ 此試驗針對的是高尿酸血症合併泌尿道結石患者，與腎性低尿酸血症（RHUC）的病生理不同，相關性為間接。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Case Report | Internal Medicine (Tokyo) | 首例報告 Febuxostat 作為 RHUC 患者 EIAKI 預防性治療：16 歲足球員補水無效，使用非嘌呤類 XOR 抑制劑後觀察到保護效果，支持減少尿液嘌呤負荷的機轉假說 |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Narrative Review | Clinical Rheumatology | 低尿酸血症（< 2 mg/dL）的病因、分類與臨床處置系統性敘述，涵蓋腎性病因（URAT1/GLUT9 缺陷）、EIAKI 風險及治療策略，提供 RHUC 的完整臨床背景 |

---

## 香港上市資訊

香港（衞生署許可證資料庫）目前查無 Febuxostat 相關藥品許可證登記，該藥在香港屬未上市狀態。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 本 Evidence Pack 的警語、禁忌症及藥物交互作用資料均為 Data Gap（DG001，Blocking 等級），尚無法完成標準 S1 安全性初評。

---

## 結論與下一步

**決策：Hold**

**理由：**
Febuxostat 用於腎性低尿酸血症預防 EIAKI 的機轉假說具備合理性，但現有直接證據僅限於個案報告層級，且该藥在香港尚未取得任何上市許可；加之安全性資料（警語、禁忌）完全缺失（Blocking 等級），依規程無法進入 S1 安全性初評。

**若要推進需要：**
- 取得 EMA、FDA 或 TFDA 原廠仿單，補齊安全性警語與禁忌症（DG001，Blocking）
- 補充 DrugBank MOA 正式資料以強化機轉關聯性分析（DG002，High）
- 尋找更多直接針對 RHUC/EIAKI 的前瞻性或隨機對照臨床試驗
- 釐清 NCT04398251 試驗最終結果（狀態「未知」，且適應症為高尿酸血症，需評估其與 RHUC 的間接相關性）
- 評估香港特殊患者用藥（Special Patient Programme）或進口申請之可行性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

