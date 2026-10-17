---
layout: default
title: Probenecid
parent: 中證據等級 (L3-L4)
nav_order: 732
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Probenecid：預測新適應症為腎性低尿酸血症 (Hypouricemia, Renal)（證據等級 L4）。原適應症：痛風、高尿酸血症"
monitor_inn: "PROBENECID"
predicted_indications: ["hypouricemia, renal", "Lesch-Nyhan syndrome", "hypoxanthine guanine phosphoribosyltransferase partial deficiency"]
---

# Probenecid
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
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

# Probenecid：從痛風到腎性低尿酸血症

## 一句話總結

Probenecid 是一種促尿酸排泄藥，原本用於痛風與高尿酸血症。
TxGNN 模型預測它可能對**腎性低尿酸血症 (Hypouricemia, Renal)** 有效，但目前**沒有臨床試驗**，僅有 **20 篇相關文獻**，且文獻多顯示 probenecid 只是診斷用探針，並非治療。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 痛風、高尿酸血症（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 腎性低尿酸血症 (Hypouricemia, Renal) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，probenecid 是促尿酸排泄藥，會抑制腎臟的 URAT1 (SLC22A12) 與 OAT1/OAT3 轉運蛋白，增加尿酸從腎臟排出，因此可用於痛風與高尿酸血症。

腎性低尿酸血症的病因，主要是 URAT1 (SLC22A12) 或 GLUT9 (SLC2A9) 功能喪失，使尿酸在腎小管重吸收不足、排泄過多。兩者涉及同一條尿酸轉運路徑，這很可能就是 TxGNN 給出高分的原因。

但這種關聯**不是治療性的**。這個疾病的問題是尿酸「已經排太多」，probenecid 只會進一步促進尿酸流失，無法矯正根本缺陷，預期無效甚至有害（可能增加運動誘發急性腎損傷與泌尿道結石的風險）。文獻中 probenecid 主要用於負荷試驗，根據尿酸清除率的反應來區分缺陷類型。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

共 20 篇文獻，以下列出最相關者（多為綜述、個案報告，無 RCT）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review | Mol Genet Metab | 遺傳性腎性低尿酸血症多由 SLC22A12 (URAT1) 功能喪失突變所致 |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clin Rheumatol | 針對風濕科醫師的低尿酸血症更新，涵蓋病因分類 |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Review/個案 | Am J Kidney Dis | 腎性低尿酸血症與運動誘發急性腎衰竭，探討預防方式 |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | 世代研究（基因分析） | J Am Soc Nephrol | 32 位患者的 SLC22A12 定序，URAT1 基因影響尿酸排泄 |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | 病例系列（生理研究） | Nephron | 患者對 probenecid 與 pyrazinamide 的尿酸清除反應減弱，提示近端小管重吸收缺陷 |
| [8976099](https://pubmed.ncbi.nlm.nih.gov/8976099/) | 1996 | Review | Nihon Rinsho | 尿酸代謝異常的概念與分類 |
| [3813739](https://pubmed.ncbi.nlm.nih.gov/3813739/) | 1987 | 病例系列 | Arch Intern Med | 糖尿病患者的腎性低尿酸血症，尿酸清除增加 |
| [1944743](https://pubmed.ncbi.nlm.nih.gov/1944743/) | 1991 | 病例系列 | Nephron | 第 1 型糖尿病合併腎性低尿酸血症 |
| [9583212](https://pubmed.ncbi.nlm.nih.gov/9583212/) | 1998 | 個案報告 | Acta Paediatr Jpn | 女童腎性低尿酸血症併運動後急性腎衰竭 |
| [2709741](https://pubmed.ncbi.nlm.nih.gov/2709741/) | 1989 | 個案報告 | Klin Wochenschr | 腎性低尿酸血症患者發生尿酸腎病變，probenecid 可增加尿酸排泄分率 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-57027 | U-ACID TAB 500MG | 未載明 | 未載明 |
| HK-16674 | PROBENECID TAB 500MG (WHITE) | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單內容，僅供參考）：肝衰竭、腎臟疾病與腎功能受損、血液疾病（血小板低下、白血球低下、顆粒球缺乏、嗜中性白血球低下等）、消化性潰瘍、肌肉病變與橫紋肌溶解症、腹瀉性疾病（含困難梭狀芽孢桿菌結腸炎）等。
- **藥物交互作用**：資料庫共記錄 71 項，以下為部分重點：
  - **嚴重 (Major)**：Phenylbutyric acid、Glycerol phenylbutyrate
  - **中度 (Moderate)**：Acetylsalicylic acid（阿斯匹靈）、磺醯脲類降血糖藥（chlorpropamide、glimepiride、glipizide、glyburide、tolbutamide、tolazamide、acetohexamide）、repaglinide、nateglinide
  - **輕微 (Minor)**：Famotidine、amoxicillin、levofloxacin、eluxadoline
- 就本預測適應症而言，需特別留意運動誘發急性腎損傷與泌尿道結石的風險。

其餘警語與禁忌的仿單資料目前缺乏，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 本預測缺乏臨床試驗，且機轉上 probenecid 會加重尿酸流失，不具治療合理性；TxGNN 高分反映的是共同轉運路徑，而非療效。
- 文獻中 probenecid 只是診斷用探針。

**若要推進需要：**
- 說明如何以機轉支持療效（目前機轉分析指向無效或有害）
- 取得完整的作用機轉資料與香港仿單的警語、禁忌
- 若仍要探索，需先進行嚴謹的安全性評估，特別是腎損傷與結石風險
- 建議改為評估其他預測適應症（如 HPRT 部分缺乏症的高尿酸血症與痛風），但該類患者尿酸產生過多，通常優先使用黃嘌呤氧化酶抑制劑，且同樣缺乏臨床證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

