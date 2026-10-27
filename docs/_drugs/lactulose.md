---
layout: default
title: Lactulose
parent: 僅模型預測 (L5)
nav_order: 504
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Lactulose：預測新適應症為急性尿酸腎病變 (Acute Urate Nephropathy)（證據等級 L5）。原適應症：肝性腦病變、肝昏迷、便秘"
monitor_inn: "LACTULOSE"
predicted_indications: ["acute urate nephropathy", "nephrolithiasis", "obstructive jaundice", "bile duct disease", "biliary tract disease"]
---

# Lactulose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Lactulose：從肝性腦病變到阻塞性黃疸
{: .text-alpha }

## 一句話總結

Lactulose（乳果糖）是一種不被吸收的雙醣，原本用於肝性腦病變、肝昏迷與便秘。
TxGNN 模型預測它可能對**急性尿酸腎病變**、**腎結石**、**阻塞性黃疸 (Obstructive Jaundice)**、**膽管疾病**與**膽道疾病**有效。
其中證據最多的是**阻塞性黃疸**：目前有 **0 個臨床試驗**，但有 **20 篇文獻**，多為小型臨床研究與動物實驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肝性腦病變、肝昏迷、便秘（取自知識圖譜，香港許可證未載明適應症文字） |
| 預測新適應症 | 急性尿酸腎病變 (Acute Urate Nephropathy)（TxGNN 排名第 1）；證據最完整者為阻塞性黃疸 |
| TxGNN 預測分數 | 99.89%（急性尿酸腎病變）；阻塞性黃疸為 99.53% |
| 證據等級 | 急性尿酸腎病變 L5；阻塞性黃疸 L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Hold（整體）；阻塞性黃疸方向可列為研究問題（Research Question） |

各預測適應症一覽：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 1 | 急性尿酸腎病變 | 99.89% | L5 | Hold |
| 2 | 腎結石 | 99.78% | L5 | Hold |
| 3 | 阻塞性黃疸 | 99.53% | L3 | Research Question |
| 4 | 膽管疾病 | 99.47% | L3 | Research Question |
| 5 | 膽道疾病 | 99.38% | L4 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Lactulose 是一種不被吸收的雙醣，在結腸被細菌發酵，臨床上用於降低腸道氨負荷（肝性腦病變）及緩解便秘。

排名第 1 與第 2 的預測（急性尿酸腎病變、腎結石）沒有任何臨床試驗或文獻支持。雖然理論上 Lactulose 可能改變腸道菌叢、含氮化合物吸收或結腸發酵後的尿液酸鹼度，但沒有資料能把這些作用與尿酸造成的腎小管損傷連結起來。該疾病的標準治療（水分補充、rasburicase、allopurinol）針對的是實際病因。

阻塞性黃疸則有較合理的機轉線索：膽管阻塞使腸道缺少膽鹽，促進內毒素吸收、細菌移位與腸道屏障受損，內毒素血症進而導致術後腎功能異常與肝損傷。Lactulose 被認為可降低腸道內毒素負荷、調整腸道菌叢並協助恢復屏障功能。膽管疾病的證據與此大量重疊，並非獨立佐證；膽道疾病則多為間接證據（如 Lactulose 與高纖飲食對膽汁組成、膽結石的影響）。

需注意：部分文獻結論並不一致。1997 年的回顧指出，Lactulose 對術後腎功能的保護效果迄今未被臨床研究確切證實；1989 年大鼠研究也顯示 Lactulose 並未預防膽汁梗塞或轉胺酶上升。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下以證據最多的**阻塞性黃疸**為主，列出最相關的文獻（本報告僅依標題與摘要片段判斷，研究設計與效果量尚待核實）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2032107](https://pubmed.ncbi.nlm.nih.gov/2032107/) | 1991 | 多中心臨床研究（前瞻性隨機試驗，設計待核實） | Br J Surg | 102 位阻塞性黃疸手術病人隨機分為術前口服 Lactulose、去氧膽酸鈉與對照組，評估術後腎功能障礙的預防 |
| [3768644](https://pubmed.ncbi.nlm.nih.gov/3768644/) | 1986 | 實驗與臨床研究 | Br J Surg | 24 位病人（12 位用 Lactulose）；治療組術中門脈與術後全身內毒素血症顯著降低 |
| [12957136](https://pubmed.ncbi.nlm.nih.gov/12957136/) | 2003 | 臨床／實驗研究 | J Surg Res | 兔子膽管結紮模型，評估 Lactulose 對內毒素血症與細菌移位的作用 |
| [23297639](https://pubmed.ncbi.nlm.nih.gov/23297639/) | 2012 | 臨床研究 | Zh Mikrobiol Epidemiol Immunobiol | 膽管減壓合併 Lactulose 對機械性黃疸病人腸道微生態的影響 |
| [8944448](https://pubmed.ncbi.nlm.nih.gov/8944448/) | 1996 | 臨床與實驗研究 | Br J Surg | 阻塞性黃疸有腸道屏障功能障礙，內引流可逆轉（背景證據） |
| [9145459](https://pubmed.ncbi.nlm.nih.gov/9145459/) | 1997 | Review | Scand J Gastroenterol Suppl | Lactulose 對術後腎功能的保護效果尚未被臨床研究確切證實 |
| [15782993](https://pubmed.ncbi.nlm.nih.gov/15782993/) | 2005 | Review | Hepato-gastroenterology | 主張術前充分水分補充與 Lactulose 以預防急性阻塞性黃疸的術後腎功能障礙 |
| [29428098](https://pubmed.ncbi.nlm.nih.gov/29428098/) | 2018 | Review | Hepatobiliary Pancreat Dis Int | 阻塞性黃疸的病理生理與圍手術期處置 |
| [12598962](https://pubmed.ncbi.nlm.nih.gov/12598962/) | 2002 | 動物研究（大鼠） | Pediatr Surg Int | 褪黑激素與 Lactulose 對阻塞性黃疸大鼠肝腎的影響 |
| [2614579](https://pubmed.ncbi.nlm.nih.gov/2614579/) | 1989 | 動物研究（大鼠） | J Pathol | Lactulose、polymyxin B、neomycin 皆未能預防膽汁梗塞與轉胺酶上升（陰性結果） |

膽道疾病方面，另有 [9145452](https://pubmed.ncbi.nlm.nih.gov/9145452/)（1997，Lactulose 與高纖飲食對膽汁與膽結石的影響回顧）和 [6269949](https://pubmed.ncbi.nlm.nih.gov/6269949/)（1981，倉鼠實驗），屬間接證據。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-43381 | PMS-LACTULOSE SOLUTION 667MG/ML | 口服溶液 | 未載明 |
| HK-67979 | LALALAX ORAL SOLUTION 10G/15ML | 口服溶液 | 未載明 |
| HK-68911 | LOLAN ORAL SOLUTION 66.7G/100ML | 口服溶液 | 未載明 |
| HK-68890 | BF-LACTULOSE ORAL SOLUTION 667MG/ML | 口服溶液 | 未載明 |
| HK-67881 | CONSIQARE ORAL SOLUTION 667MG/ML | 口服溶液 | 未載明 |

香港共有 13 張有效許可證（全為單方），尚無已註銷者；以上僅列出 5 張。

---

## 安全性考量

- **知識圖譜標示的相關疾病（非仿單內容）**：糖尿病、糖尿病酮酸中毒、闌尾炎、半乳糖血症、肝醣儲積症、G6PD 缺乏症、胱胺酸尿症、葡萄糖－半乳糖吸收不良。
- **藥物交互作用**：共查得 100 筆，以下為部分範例，多數為中度：Abiraterone、Tramadol、Acetazolamide、Hydrocortisone、Salbutamol、Hydrochlorothiazide、Amiloride、Amiodarone、Triamcinolone、Arsenic trioxide。另有輕度交互作用如 Sodium citrate。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（阻塞性黃疸方向可列為 Research Question）**

**理由：**
- 排名最高的兩項預測（急性尿酸腎病變、腎結石）僅有模型分數，沒有任何臨床試驗或文獻支持，機轉上也缺乏連結。
- 阻塞性黃疸有 1980–2000 年代的小型臨床與動物研究（證據等級 L3），但結果不一致，且沒有已登記的臨床試驗；膽管疾病的證據與其高度重疊，膽道疾病則多為間接證據。

**若要推進需要：**
- 審閱阻塞性黃疸文獻的完整摘要與全文，確認 1991 年多中心研究的設計（是否為隨機對照）與效果量，再決定是否升級證據等級。
- 補充 Lactulose 詳細的作用機轉資料（MOA）。
- 取得香港衛生署仿單的警語與禁忌症（目前缺漏，為阻擋安全性篩選的關鍵缺口）。
- 對照現行圍手術期處置（如充分水分補充、膽道引流），評估 Lactulose 是否有額外價值，並考慮設計現代的前瞻性對照試驗。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

