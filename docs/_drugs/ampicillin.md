---
layout: default
title: Ampicillin
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 9
monitor_inn: "AMPICILLIN"
predicted_indications: ["laryngitis", "Ureaplasma urethritis", "chronic rhinosinusitis", "chronic ethmoidal sinusitis", "gingivitis", "paranasal sinus neoplasm (disease)", "bacterial arthritis", "conjunctivitis", "pericoronitis"]
last_modified_at: 2026-11-24
description: "Ampicillin：預測新適應症為喉炎 (laryngitis)（證據等級 L5）。香港藥劑製品註冊：32 張（有效 31 張）"
---

# Ampicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Ampicillin：β-內醯胺類抗生素（抑制細菌細胞壁合成） → 喉炎 (laryngitis)
{: .text-alpha }

## 一句話總結

Ampicillin 是一種廣效型 β-內醯胺類（青黴素類）抗生素，用於多種細菌感染。
TxGNN 模型預測它可能對**喉炎 (laryngitis)** 有效，
但目前**沒有臨床試驗**，且檢索到的文獻多為病例報告、回顧與無直接關聯的主題，**沒有直接研究 ampicillin 治療喉炎的證據**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 喉炎 (laryngitis) |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 31 張／共 32 張） |
| 許可證數 | 32 張（有效 31 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Ampicillin 透過抑制細菌細胞壁合成而殺菌。根據美國 FDA 核准的 Ampicillin 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Ampicillin 對處於活躍繁殖期的敏感細菌所具有的殺菌作用與 penicillin 相似。其作用是透過抑制細胞壁生物合成，進而導致細菌死亡。」英文原文："Ampicillin is similar to penicillin in its bactericidal action against susceptible bacteria during the stage of active multiplication. It acts through the inhibition of cell wall biosynthesis that leads to the death of the bacteria."（[DailyMed: ampicillin prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4134cd79-c895-4e6e-b1d5-8e01c38bf2d1)，版本日期 2026-07-27；查閱日期 2026-11-19）。

細菌性喉部感染（例如由 *Haemophilus influenzae* 引起的會厭炎）理論上可能對 ampicillin 敏感，這是模型預測在機轉上的可能connection。但近年許多 *H. influenzae* 菌株會產生 β-內醯胺酶而對 ampicillin 產生抗藥性，限制了經驗性使用。

此外，喉炎多為病毒性或非感染性，抗生素並非一般首選。模型的高分並未獲得直接臨床試驗證據支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下列文獻涉及喉部、會厭或相關頸部感染，但**均非直接評估 ampicillin 治療喉炎**的研究：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | Review | Anaesth Intensive Care | 161 名兒童急性會厭炎病歷回顧，重點在氣道處置與併發症 |
| [2603419](https://pubmed.ncbi.nlm.nih.gov/2603419/) | 1989 | Review | West J Med | 成人會厭炎 9 例，常初診誤判，部分需插管 |
| [3026014](https://pubmed.ncbi.nlm.nih.gov/3026014/) | 1986 | 未分類 | Rev Infect Dis | 討論 sulbactam/ampicillin 用於兒童急性會厭炎；約 25% Hib 菌株對 ampicillin 抗藥 |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | Case report | Ann Otol Rhinol Laryngol | 自發性喉膿瘍病例與文獻回顧 |
| [34986973](https://pubmed.ncbi.nlm.nih.gov/34986973/) | 2023 | Case report | Auris Nasus Larynx | COVID-19 相關急性會厭炎病例 |
| [25944348](https://pubmed.ncbi.nlm.nih.gov/25944348/) | 2015 | Cohort | Otolaryngol Head Neck Surg | 喉切除術圍手術期抗生素選擇與併發症的關聯 |
| [3290661](https://pubmed.ncbi.nlm.nih.gov/3290661/) | 1988 | 未分類 | Monatsschr Kinderheilkd | Hib 對 ampicillin 抗藥性改變所帶來的會厭炎治療調整 |
| [6881564](https://pubmed.ncbi.nlm.nih.gov/6881564/) | 1983 | 未分類 | Anesth Analg | 23 名兒童會厭炎插管時間，以 ampicillin 或 chloramphenicol 治療 |

## 香港上市資訊

香港含本藥成分的許可證包括單一成分與複方製劑，張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表，主要如下：

<!-- review:begin hk-lic-20261117-ampicillin-1 -->

> **查核更正（2026-11-24）**：原文為「香港共有多張含 ampicillin 單方成分的有效許可證（資料可能不完整），」。已更正：HK-40801 已不列於衞生署藥物辦公室的註冊藥劑製品名單，網上藥物資料庫也查不到，已不是現行註冊（2026-11-17 核對）。 已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊；含本藥成分的許可證包括單一成分與複方製劑，張數見本頁快速總覽與許可證表（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html)。

<!-- review:end hk-lic-20261117-ampicillin-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-10610 | A P CAP 250MG | 單一成分 | THE UNITED LABORATORIES LTD | 有效 |
| HK-63787 | AMPICILLIN POWDER FOR SOLUTION FOR INJECTION 500MG | 單一成分 | CEUTICAL TRADING COMPANY LIMITED | 有效 |
| HK-61293 | NORAPILIN POWDER FOR SOLUTION FOR IM/IV INJECTION 500MG | 單一成分 | JINDUN PHARMA (H.K.) LIMITED | 有效 |
| HK-40801 | PAMECIL FORTE FOR SYRUP 250MG/5ML | 單一成分 | STAR MEDICAL SUPPLIES LTD | 已註銷 |
| HK-56898 | AMPICILLIN SODIUM FOR INJ 0.5G | 單一成分 | REGAL MEDICAL HEALTHCARE LIMITED | 有效 |

上表列出其中 5 張（共 32 張）。

<!-- licenses:end -->

## 安全性考量

- **藥物交互作用**：共 61 筆交互作用紀錄，中度者包括 Doxycycline、Minocycline、Tetracycline、Kanamycin、Balsalazide、Lansoprazole、Dexlansoprazole、Picosulfuric acid；Clarithromycin 為輕度。

其餘警語與禁忌症資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何直接研究 ampicillin 治療喉炎的臨床試驗或文獻，證據等級僅為 L5；高分預測僅來自模型。
- 會厭炎的主要病原菌 *H. influenzae* 常有 β-內醯胺酶抗藥性，且喉炎多為病毒性，抗生素的角色有限。

**若要推進需要：**
- 針對喉炎（區分細菌性與病毒性）的直接臨床研究或回溯性療效資料
- 當地 *H. influenzae* 等病原菌對 ampicillin 的抗藥性監測資料
- 取得原廠仿單的警語、禁忌症與作用機轉資料
- 與現有標準治療（如第三代頭孢菌素、含 β-內醯胺酶抑制劑的複方）的比較

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「香港共有多張含 ampicillin 單方成分的有效許可證（資料可能不完整），」→「香港含本藥成分的許可證包括單一成分與複方製劑，張數與有效張數」 | 更正（2026-11-24 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: ampicillin prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4134cd79-c895-4e6e-b1d5-8e01c38bf2d1) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

