---
layout: default
title: Nystatin
parent: 中證據等級 (L3-L4)
nav_order: 621
evidence_level: L3
indication_count: 5
---

# Nystatin
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Nystatin：從抗真菌治療到外陰陰道炎

## 一句話總結

Nystatin（制黴菌素）是多烯類（polyene）抗真菌藥，香港已有多張製劑許可證。
TxGNN 模型預測它可能對**外陰陰道炎 (Vulvovaginitis)** 有效，目前有 **0 個相關臨床試驗**，但有 **20 篇文獻**（以綜述和觀察性研究為主）。
這個預測很可能是既有的標示用途，並非全新的老藥新用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 外陰陰道炎 (Vulvovaginitis) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

香港許可證資料中沒有提供核准適應症文字，因此「原適應症」欄位省略。

---

## 為什麼這個預測合理？

目前 DrugBank 的作用機轉欄位是空的。根據藥物類別判斷，Nystatin 是多烯類抗真菌藥，會結合真菌細胞膜上的麥角固醇（ergosterol）並形成孔洞。孔洞造成細胞內容物滲漏，真菌因而死亡。

外陰陰道炎中最常見的一類是念珠菌感染（外陰陰道念珠菌症），約 85–90% 由白色念珠菌引起。Nystatin 的抗真菌機轉直接對應這類感染，所以 TxGNN 給出很高的分數，與藥理上的預期一致。

需要注意兩點：
- 這個預測很可能是既有的標示用途。「原適應症」和「作用機轉」為空，應視為資料缺口，不宜當成新發現。
- Nystatin 對非真菌性的外陰陰道炎（如細菌性陰道炎、滴蟲感染）沒有作用。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

本次資料中沒有識別出 RCT。下表依證據強度排序，「類型」欄中的動物實驗與體外研究是依摘要內容判讀。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | 世代研究 | Mycoses | 分析 287 株複雜性外陰陰道念珠菌症的分離株，比較 fluconazole 與 nystatin 的體外感受性和臨床結果的關聯 |
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | 回顧 fluconazole 抗藥性外陰陰道念珠菌症的處置，替代療法包括硼酸、nystatin、oteseconazole、ibrexafungerp |
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clinical Evidence | 外陰陰道念珠菌症是僅次於細菌性陰道炎的第二常見陰道炎，白色念珠菌佔 85–90% |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Womens Health | 復發性外陰陰道念珠菌症的硼酸臨床證據，非白色念珠菌對 azole 類較不敏感 |
| [21718579](https://pubmed.ncbi.nlm.nih.gov/21718579/) | 2010 | Review | BMJ Clinical Evidence | 外陰陰道念珠菌症的證據回顧（早期版本） |
| [12228137](https://pubmed.ncbi.nlm.nih.gov/12228137/) | 2002 | Review | BMJ | 外陰陰道念珠菌症綜述（無摘要） |
| [19454049](https://pubmed.ncbi.nlm.nih.gov/19454049/) | 2007 | Review | BMJ Clinical Evidence | 外陰陰道念珠菌症的證據回顧（早期版本） |
| [1436934](https://pubmed.ncbi.nlm.nih.gov/1436934/) | 1992 | Review | Obstet Gynecol Clin North Am | Nystatin 於 1950 年代用於外陰陰道念珠菌症，後來被 imidazole 和 triazole 類取代成為首選 |
| [30359236](https://pubmed.ncbi.nlm.nih.gov/30359236/) | 2018 | 動物實驗 | BMC Microbiology | 大鼠模型顯示 nystatin 可增強對白色念珠菌的黏膜免疫反應，並保護陰道上皮超微結構 |
| [32104010](https://pubmed.ncbi.nlm.nih.gov/32104010/) | 2020 | 體外研究 | Infect Drug Resist | 測試氧化鋅奈米粒子和 nystatin 對抗 fluconazole 抗藥性白色念珠菌分離株的活性 |

---

## 香港上市資訊

共 20 張許可證，以下列出 5 張。許可證資料未提供劑型與核准適應症文字，劑型是依品名判讀。

| 許可證號 | 品名 | 劑型（依品名判讀） | 廠商 |
|---------|------|------|------|
| HK-44908 | PMS-NYSTATIN SUSP 100000U/ML | 懸液劑 | TRENTON-BOMA LTD |
| HK-58764 | NYDASIN VAGINAL SUPP 100,000U | 陰道栓劑 | YAT SENG TRADING CO |
| HK-45763 | NYSTATIN OINTMENT 100000IU/G | 軟膏 | HON MAN MEDICINE (WING LEE) COMPANY |
| HK-34420 | NYSTATIN CAP 500000U | 膠囊劑 | YUNG SHIN CO LTD |
| HK-34392 | NYSTATIN VAG TAB 100000U | 陰道錠 | YUNG SHIN CO LTD |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 機轉與念珠菌性外陰陰道炎高度吻合，文獻也支持（L3：綜述加觀察性研究），香港已有陰道栓劑和陰道錠等製劑上市。
- 但沒有 RCT 或臨床試驗資料，安全性資料也缺漏，因此不能給出無條件的 Go。

**使用防護（Guardrails）：**
- 使用前先確認病因為念珠菌，Nystatin 對細菌性或滴蟲性外陰陰道炎無效。
- Fluconazole 抗藥或非白色念珠菌感染需另行處置。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌症和核准適應症（目前是阻擋性資料缺口）。
- 從 DrugBank 補齊作用機轉。
- 回到來源文章確認 BMJ Clinical Evidence 等綜述是否納入 RCT，作為證據升級（L1/L2）的依據。

**其他預測：**
排名 2–5 的預測（眼眶區域疾病、眼附屬器眶部疾病、囊性畸胎瘤、脊髓皮樣囊腫）沒有機轉依據或臨床證據，全部建議 **Hold**。排名 2 所配對的兩個試驗與 Nystatin 無關。

本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

