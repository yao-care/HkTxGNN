---
layout: default
title: Mycophenolate Mofetil
parent: 僅模型預測 (L5)
nav_order: 603
evidence_level: L5
indication_count: 10
monitor_inn: "MYCOPHENOLATE MOFETIL"
predicted_indications: ["HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "bone Paget disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "multiple sclerosis", "hemosiderosis", "Heiner syndrome", "African iron overload", "neonatal hemochromatosis"]
last_modified_at: 2026-10-31
description: "Mycophenolate Mofetil：預測新適應症為HIV 感染 (HIV infectious disease)（證據等級 L5）。原適應症：本報告所編資料未載明"
---

# Mycophenolate Mofetil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Mycophenolate Mofetil：從原適應症資料缺漏到 HIV 感染
{: .text-alpha }

## 一句話總結

Mycophenolate Mofetil（嗎替麥考酚酯，MMF）是一種免疫抑制劑，本報告所編資料中未載明其香港核准適應症。
TxGNN 模型預測它可能對 **HIV 感染 (HIV infectious disease)** 有效，
目前有 **4 個臨床試驗**登記（其中直接相關者僅 1 個，且已撤回、無受試者）和 **20 篇文獻**，但直接的人體療效證據有限。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本報告所編資料未載明（香港許可證的適應症文字皆為空白） |
| 預測新適應症 | HIV 感染 (HIV infectious disease) |
| TxGNN 預測分數 | 0.9986 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 建議決策 | Hold |

**證據等級說明：** 資料中雖有 MMF 用於 HIV 的小型研究（例如 PMID 15353978 的隨機試驗），但這些研究的主要目的是探討抗病毒或免疫效應，並未提供療效已確立的證據；已登記的 Phase 2 試驗（NCT00021489）已撤回、無受試者，其餘試驗只是間接相關。依規則，為保守起見，本報告將證據等級定為 **L5**。這低於資料中自動評分給出的 L2，後者與實際可用的直接證據不相稱。

## 為什麼這個預測合理？

本報告所編資料缺乏正式的作用機轉欄位。根據文獻推論，麥考酚酸（MMF 的活性代謝物）會抑制 IMPDH，使淋巴球內的鳥苷核苷酸減少，進而降低 T 細胞增殖。

這在 HIV 上有兩個可能的作用：
1. 減少活化的 CD4 T 細胞，這類細胞是 HIV 複製的標的。
2. 鳥苷核苷酸（dGTP）減少，可能增強 abacavir、didanosine 等鳥苷類似物抗病毒藥的活性。

早期小型研究（如 PMID 12352149，僅 5 位患者）觀察到加入 MMF 後血漿 HIV-1 RNA 下降；另一項研究（PMID 16379601）顯示 MMF 加 HAART 未見明顯不利的免疫影響。不過，免疫抑制劑用於 HIV 患者仍有感染風險，這是核心的安全疑慮。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 2 | 撤回 | 0 | MMF 併用 abacavir 治療 HIV 的安全性與抗病毒活性；未收案，無數據 |
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 2 | 完成 | 56 | DAPD 與 DAPD 加 MMF 用於已治療過的 HIV 患者；MMF 非唯一介入，間接相關 |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | 提前終止 | 8 | 環孢素加 MMF 治療抗 EPO 相關純紅血球再生不良；與 HIV 關聯薄弱 |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | 不適用 | 完成 | 5 | HIV 陽性患者異體幹細胞移植，MMF 為移植後免疫抑制的一部分；間接相關 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | RCT | AIDS | 未曾治療的 HIV-1 患者，HAART 加或不加 MMF，比較血漿 HIV RNA 下降速度與潛伏儲存庫 |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | 臨床藥動/藥效研究 | Clin Pharmacokinet | 低劑量 MMF 併用 abacavir、efavirenz、nelfinavir 的藥動學與藥效學 |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | 臨床研究 | AIDS Res Hum Retroviruses | MMF 加 HAART 未見明顯不利的免疫學影響 |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | 小型病例系列 | J Acquir Immune Defic Syndr | 5 位治療失敗患者加入 MMF，細胞內 dGTP 下降，血漿 HIV-1 RNA 降低 |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | 免疫抑制藥物在 HIV 疾病中的角色 |
| [16515490](https://pubmed.ncbi.nlm.nih.gov/16515490/) | 2006 | Review | Curr Pharm Des | 以病毒抑制劑（virostatics）作為 HIV 治療策略 |
| [20840478](https://pubmed.ncbi.nlm.nih.gov/20840478/) | 2010 | 回溯性研究 | Am J Transplant | 巴黎 27 位 HIV 感染者腎臟移植經驗，免疫抑制方案含 MMF |
| [19112763](https://pubmed.ncbi.nlm.nih.gov/19112763/) | 2008 | 病例報告 | J Drugs Dermatol | HIV 合併乾癬與乾癬性關節炎患者使用 MMF 有效且安全 |

## 香港上市資訊

本報告所編資料列出至少 20 張單一成分許可證（清單可能不完整），以下為其中 5 張：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44333 | CELLCEPT TAB 500MG（羅氏） | 錠劑 | 資料未載明 |
| HK-41757 | CELLCEPT CAP 250MG（羅氏） | 膠囊 | 資料未載明 |
| HK-62451 | CELLCEPT POWDER FOR ORAL SUSPENSION 1G/5ML（羅氏） | 口服懸液用粉末 | 資料未載明 |
| HK-59026 | MICOCEPT TAB 500MG（山德士） | 錠劑 | 資料未載明 |
| HK-65892 | ACCORD MYCOPHENOLATE MOFETIL POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 500MG | 輸注濃縮液用粉末 | 資料未載明 |

## 安全性考量

- **知識圖譜記錄的禁忌關係（非仿單內容）：** 知識圖譜中與本藥相連的禁忌疾病包括肝病、膽囊疾病、嗜中性白血球低下、顆粒球缺乏症、活動性消化性潰瘍、巨細胞病毒感染、單純皰疹、帶狀皰疹、進行性多灶性白質腦病、淋巴瘤、皮膚癌、再生不良性貧血及多種先天性骨髓衰竭症候群等。
- **藥物交互作用：** 共查得 92 筆。其中 **重大** 等級者包括活性碳；**中度** 等級者包括質子幫浦抑制劑（rabeprazole、omeprazole、esomeprazole、lansoprazole、dexlansoprazole）、抗生素（doxycycline、amoxicillin、tetracycline、clarithromycin、minocycline、vancomycin、kanamycin、paromomycin）及制酸劑（氧化鎂、氫氧化鋁、碳酸鈣）；鋅鹽與鐵劑屬 **輕微** 等級。
- **HIV 情境下的特別考量：** 免疫抑制可能加重 HIV 患者的機會性感染風險，且 MMF 有致畸胎性（資料中於新生兒血色素沉著症項下提及）。

主要警語與正式禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 雖然 TxGNN 分數很高，機轉上也有合理性，但直接評估 MMF 治療 HIV 的臨床試驗僅有一個且已撤回、無數據，其餘為小型或間接研究，無法支持療效。
- 對 HIV 患者使用免疫抑制劑本身存在感染風險，在缺乏確切療效證據下，不建議推進。

**若要推進需要：**
- 取得香港仿單，確認核准適應症、警語與禁忌症
- 補充 MMF 的正式作用機轉資料
- 設計並執行足夠樣本數的 HIV 隨機對照試驗，評估病毒學與免疫學終點
- 制訂針對 HIV 族群的機會性感染監測與安全性計畫

## 其他預測適應症簡述

- **多發性硬化症 (multiple sclerosis)**：TxGNN 分數 0.9954。有 Phase 2 及 Phase 2/3 小型試驗、Cochrane 系統性回顧與回溯性研究（344 位患者）支持，直接研究此疾病，值得獨立評估，惟樣本小，MMF 並非既有的多發性硬化症疾病修飾療法。
- **含鐵血黃素沉著症 (hemosiderosis)**：僅有回顧與病例層級文獻，無臨床試驗。
- 其餘預測（如帕哲氏骨病、貓與猴免疫缺乏病毒、Heiner 症候群、非洲鐵過載、新生兒血色素沉著症等）僅有模型預測，無試驗或文獻支持。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

