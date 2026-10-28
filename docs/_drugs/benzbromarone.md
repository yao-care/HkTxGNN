---
layout: default
title: Benzbromarone
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 1
monitor_inn: "BENZBROMARONE"
predicted_indications: ["hypouricemia, renal"]
last_modified_at: 2026-10-27
description: "Benzbromarone：預測新適應症為腎性低尿酸血症 (hypouricemia, renal)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Benzbromarone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Benzbromarone：URAT1 抑制型促尿酸排泄藥 → 腎性低尿酸血症 (hypouricemia, renal)
{: .text-alpha }

## 一句話總結

Benzbromarone 是一種 URAT1 抑制劑，透過阻斷腎臟對尿酸的再吸收來降低血中尿酸。
TxGNN 模型預測它可能與**腎性低尿酸血症 (hypouricemia, renal)** 有關，但目前沒有任何臨床試驗，僅有 **19 篇文獻**，且多為病例報告與生理試驗，並非治療性研究。依機轉判斷，這很可能是偽陽性預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 腎性低尿酸血症 (hypouricemia, renal) |
| TxGNN 預測分數 | 0.9907 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原廠與資料庫未提供 MOA 欄位），以下為依文獻所做的機轉推論。Benzbromarone 是強效的 URAT1（SLC22A12）抑制劑，能阻斷腎小管對尿酸的再吸收，增加尿酸排泄。

腎性低尿酸血症本身正是由 URAT1（或 GLUT9）功能喪失變異所造成，表現為尿酸排泄過多、血清尿酸偏低。因此 benzbromarone 的藥理作用是**模擬疾病機轉，而非矯正它**。0.9907 的高分很可能反映模型中藥物標靶與疾病基因共享 URAT1 這個節點，而不是真正的治療關聯。

若將 benzbromarone 用於此病，預期會加重表型，增加運動誘發急性腎損傷與泌尿道結石的風險。這應視為偽陽性預測，帶有禁忌訊號，而非藥物再利用機會。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下列文獻皆未以 benzbromarone 作為治療此病的介入。多數是將 benzbromarone 當作診斷試驗（與 pyrazinamide 合用，分辨尿酸轉運缺陷部位）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | 低尿酸血症的病因分類與臨床處置更新 |
| [8976099](https://pubmed.ncbi.nlm.nih.gov/8976099/) | 1996 | Review | Nihon Rinsho | 尿酸代謝異常的概念與分類 |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | 世代／基因分析 | JASN | 日本腎性低尿酸血症患者，SLC22A12（URAT1）基因與尿酸排泄的關聯 |
| [4009341](https://pubmed.ncbi.nlm.nih.gov/4009341/) | 1985 | 病例系列 | J Pediatr | 遺傳性腎性低尿酸血症兒童，benzbromarone 與 pyrazinamide 不改變清除率比值 |
| [10879667](https://pubmed.ncbi.nlm.nih.gov/10879667/) | 2000 | 病例系列 | Clin Nephrol | 腎性低尿酸血症合併運動誘發急性腎衰竭與慢性腎功能不全 |
| [8863890](https://pubmed.ncbi.nlm.nih.gov/8863890/) | 1996 | 病例報告 | Acta Paediatr | 反覆運動誘發急性腎衰竭；以 benzbromarone/pyrazinamide 試驗判斷再吸收缺陷 |
| [3380222](https://pubmed.ncbi.nlm.nih.gov/3380222/) | 1988 | 病例報告／生理研究 | Nephron | 孤立性腎臟尿酸轉運缺陷，給予 benzbromarone 後尿酸清除率更為增加 |
| [9144014](https://pubmed.ncbi.nlm.nih.gov/9144014/) | 1997 | 病例報告 | Internal Medicine | 兩例合併腎結石，benzbromarone 抑制試驗使清除率比值上升 |
| [11676906](https://pubmed.ncbi.nlm.nih.gov/11676906/) | 2001 | 病例報告 | An Esp Pediatr | 12 個月男嬰膀胱尿酸結石，對 benzbromarone 有反應，符合再吸收前缺陷 |
| [14747372](https://pubmed.ncbi.nlm.nih.gov/14747372/) | 2004 | 前臨床（小鼠） | JASN | 小鼠 URAT1 同源蛋白的位置與尿酸轉運功能 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-29832 | NARCARICIN MITE TAB 50MG | 未記載 | 未記載 |
| HK-37906 | NARCARICIN CAP 50MG | 未記載 | 未記載 |
| HK-58488 | EURICON TAB 50MG | 未記載 | 未記載 |

## 安全性考量

安全性資訊請參考原廠仿單。

另依文獻與機轉推論，benzbromarone 促進尿酸排泄的作用，在腎性低尿酸血症患者可能加重尿酸流失，進而增加運動誘發急性腎損傷與尿酸結石的風險。這是推論，並非仿單內容。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，文獻也沒有直接評估 benzbromarone 治療此病；其在文獻中僅作為診斷用藥理探針，證據等級為 L5。
- 藥物機轉與疾病成因方向相同（皆為 URAT1 功能抑制／喪失），高分很可能是偽陽性，不建議推進。

**若要推進需要：**
- 補充 benzbromarone 的完整作用機轉資料與香港仿單的警語、禁忌症
- 以藥理與基因證據釐清模型高分是否僅來自共享的 URAT1 節點
- 在任何臨床考量之前，先確認此用途沒有加重腎損傷與結石的安全疑慮
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

