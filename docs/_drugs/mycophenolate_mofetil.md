---
layout: default
title: Mycophenolate Mofetil
parent: 僅模型預測 (L5)
nav_order: 603
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Mycophenolate Mofetil：預測新適應症為HIV 感染 (HIV infectious disease)（證據等級 L5）。原適應症：本次資料未收錄"
---

# Mycophenolate Mofetil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Mycophenolate Mofetil：從器官移植排斥反應到 HIV 感染

## 一句話總結

Mycophenolate Mofetil（MMF）是一種免疫抑制劑，在香港已有 20 張有效許可證（本次資料未收錄核准適應症文字）。
TxGNN 模型預測它可能對 **HIV 感染 (HIV infectious disease)** 有效，
目前有 **4 個臨床試驗**和 **20 篇文獻**與此方向相關，但直接證據薄弱，且臨床研究未顯示明確的持續病毒學效益。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次資料未收錄 |
| 預測新適應症 | HIV 感染 (HIV infectious disease) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L2（依系統評分；但納入的試驗多為間接或未提供數據，實際證據偏弱） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold（列為研究問題） |

## 為什麼這個預測合理？

MMF 的活性代謝物 mycophenolic acid 會抑制肌苷單磷酸脫氫酶（IMPDH），使細胞內鳥苷核苷酸減少，進而抑制淋巴球增殖。鳥苷核苷酸減少也會降低 HIV 反轉錄所需的受質。

此外，MMF 可能改變 dGTP/dATP 比例，增強 abacavir、didanosine 等核苷類似物的活性。這提供了抗病毒與免疫調節兩方面的合理依據。HIV 疾病進展也與慢性免疫活化有關，這是另一個可能的連結。

然而，臨床結果並不一致。例如在未治療過的 HIV-1 患者中比較 HAART 加或不加 MMF 的隨機試驗（PMID 15353978），並未顯示明確的持續病毒學效益。目前的支持主要來自機轉推論與小型研究。

另外需說明，本次資料未收錄 MMF 的原適應症與詳細作用機轉欄位，上述機轉說明來自預測分析的推論。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 2 | 完成 | 56 | DAPD 與 DAPD 加 MMF 用於已接受過治療的 HIV 患者；受試的主要是核苷類似物，屬間接證據 |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | 提前終止 | 8 | 環孢素加 MMF 治療抗 EPO 相關純紅血球再生不良；與 HIV 治療無關，樣本極少 |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | 完成 | 5 | HIV 陽性患者的異體幹細胞移植；MMF 僅為免疫抑制方案的一部分 |
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 2 | 撤銷 | 0 | MMF 併用 abacavir 治療 HIV 治療失敗者；直接相關但未收案，無數據 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | RCT | AIDS | 未治療過的 HIV-1 患者在 HAART 加或不加 MMF，評估對病毒 RNA 下降與潛伏儲存庫的影響 |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | PK/PD 臨床研究 | Clinical Pharmacokinetics | 低劑量 MMF 併用 abacavir、efavirenz、nelfinavir，建議進行藥動學／藥效學監測 |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | 臨床研究 | AIDS Res Hum Retroviruses | MMF 併用 HAART 未見明顯不利的免疫學影響 |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | 小型病例系列 | J Acquir Immune Defic Syndr | 5 位治療失敗患者加用 MMF 後，細胞內 dGTP 下降，血漿 HIV-1 RNA 降低 |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | 探討免疫抑制藥物在 HIV 疾病中的角色 |
| [16515490](https://pubmed.ncbi.nlm.nih.gov/16515490/) | 2006 | Review | Curr Pharm Des | 以 virostatics 作為 HIV 治療策略的回顧 |
| [12003181](https://pubmed.ncbi.nlm.nih.gov/12003181/) | 2002 | Review | J Biol Regul Homeost Agents | 免疫調節在長期控制 HIV-1 感染中的潛在角色 |
| [20840478](https://pubmed.ncbi.nlm.nih.gov/20840478/) | 2010 | 回溯性研究 | Am J Transplant | 巴黎 27 位 HIV 感染者腎臟移植經驗，維持方案含 MMF |
| [23622672](https://pubmed.ncbi.nlm.nih.gov/23622672/) | 2013 | 世代／Review | Transplant Proc | 西班牙醫院 HIV 感染者腎臟移植經驗與文獻回顧 |
| [19112763](https://pubmed.ncbi.nlm.nih.gov/19112763/) | 2008 | 病例報告 | J Drugs Dermatol | HIV 患者的乾癬與乾癬性關節炎，使用 MMF 治療安全且有效 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44333 | CELLCEPT TAB 500MG（Roche） | 錠劑 | 本次資料未收錄 |
| HK-41757 | CELLCEPT CAP 250MG（Roche） | 膠囊 | 本次資料未收錄 |
| HK-62451 | CELLCEPT POWDER FOR ORAL SUSPENSION 1G/5ML（Roche） | 口服懸液用粉末 | 本次資料未收錄 |
| HK-59026 | MICOCEPT TAB 500MG（Sandoz） | 錠劑 | 本次資料未收錄 |
| HK-65892 | ACCORD MYCOPHENOLATE MOFETIL POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 500MG（Jacobson Marketing） | 輸注濃縮液用粉末 | 本次資料未收錄 |

（共 20 張有效單一成分許可證，上表僅列 5 張主要許可證。）

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物與疾病關聯資料，並非仿單文字）：肝病、膽囊疾病、嗜中性白血球低下、顆粒球缺乏症、活動性消化性潰瘍、再生不良性貧血（含多種遺傳性類型）、巨細胞病毒感染、單純疱疹、帶狀疱疹、進行性多灶性白質腦病、淋巴瘤（含原發性中樞神經系統淋巴瘤）、皮膚癌等。對 HIV 族群而言，感染與血球低下相關項目尤需留意。
- **藥物交互作用**：共查得 92 筆，以下為部分範例：
  - 重大：活性碳（Activated charcoal）
  - 中度：質子幫浦抑制劑（rabeprazole、omeprazole、esomeprazole、lansoprazole、dexlansoprazole）、抗生素（doxycycline、amoxicillin、tetracycline、minocycline、clarithromycin、vancomycin、paromomycin、kanamycin）、制酸劑（氧化鎂、氫氧化鋁、碳酸鈣）
  - 輕微：鋅鹽、鐵
  - 若併用抗反轉錄病毒藥物（如 abacavir、efavirenz、nelfinavir），應特別評估交互作用。

仿單的警語與禁忌資料請參考原廠仿單。

## 結論與下一步

**決策：Hold（列為研究問題）**

**理由：**
- 機轉上合理（IMPDH 抑制、鳥苷耗竭、增強核苷類似物），但已有的臨床研究並未顯示明確的持續病毒學效益。
- 納入的 4 個試驗中，唯一直接測試 MMF 於 HIV 的試驗已撤銷、無受試者，其餘為間接或無關的試驗。系統評分雖為 L2，實際證據強度較低。
- 現有抗反轉錄病毒療法已相當成熟，MMF 的免疫抑制作用在 HIV 患者中可能帶來感染與血球低下風險。

**若要推進需要：**
- 取得 MMF 作用機轉與香港核准適應症的完整資料
- 取得仿單的警語與禁忌資料，完成安全性初步篩選
- 重新檢視 PMID 15353978 等既有試驗的完整數據，確認是否存在特定亞群的效益
- 評估是否有必要設計針對潛伏儲存庫或免疫活化的小型探索性試驗
- 與抗反轉錄病毒藥物併用時，建立藥物交互作用與血球監測計畫

**其他預測適應症（皆為 Hold）：** 伴有共濟失調步態、無語言與皮質白質減少的神經發育疾患、骨 Paget 病、貓後天免疫缺乏症候群、猿猴免疫缺乏病毒感染。這些目前僅有模型預測，無臨床試驗或文獻支持（L5），其中後兩者屬動物疾病，不在人類藥物再利用範圍內。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

