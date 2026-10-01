---
layout: default
title: Entecavir
parent: 中證據等級 (L3-L4)
nav_order: 318
evidence_level: L4
indication_count: 10
---

# Entecavir
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Entecavir：從慢性B型肝炎到慢性C型肝炎

## 一句話總結

Entecavir 是核苷類似物抗病毒藥，原本用於慢性B型肝炎（HBV）治療。
TxGNN 模型預測它可能對**慢性C型肝炎病毒感染 (Chronic Hepatitis C Virus Infection)** 有效。
不過資料庫中的試驗與文獻幾乎都是 B 型肝炎研究，**沒有直接證明 entecavir 對 C 型肝炎有效的證據**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性B型肝炎（香港許可證資料未附適應症文字，此項依藥理資料判斷） |
| 預測新適應症 | 慢性C型肝炎病毒感染 (Chronic Hepatitis C Virus Infection) |
| TxGNN 預測分數 | 99.98%（模型排名 855） |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Entecavir 是鳥嘌呤核苷類似物，在體內轉為三磷酸型後與 dGTP 競爭，抑制 HBV 聚合酶的引發、反轉錄與 DNA 合成。目前缺乏更詳細的作用機轉資料（DrugBank 的 MOA 欄位未取得）。

B 型與 C 型肝炎同屬病毒性肝炎，在知識圖譜中共享許多相鄰節點，模型分數偏高很可能來自這種網絡相似性。但 C 型肝炎病毒靠 RNA 依賴性 RNA 聚合酶 (NS5B) 複製，而 entecavir 作用於 HBV 聚合酶，目前沒有已確立的直接抗 HCV 活性。

臨床上唯一有關聯的情境是 **HBV/HCV 共感染**：entecavir 處理的是 B 肝部分，而不是 C 肝。因此這個預測較像是模型的網絡關聯，機轉上缺乏支持。

## 臨床試驗證據

以下試驗皆未以 HCV 療效為主要終點，多為 HBV 研究或共感染情境，僅列出相對相關者供參考。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | 完成 | 23 | HCV/HBV 共感染者接受抗 HCV 直接作用抗病毒藥時，觀察 HBV 再活化；不能證明 entecavir 抗 HCV |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | 不適用 | 未知 | 60 | HCV/HBV 共感染者接受 DAA 治療時，預防性使用核苷(酸)類似物能否預防 HBV 再活化 |
| [NCT01270178](https://clinicaltrials.gov/study/NCT01270178) | 不適用 | 未知 | 420 | 肝癌患者接受射頻消融後使用 entecavir 治療 B 肝 |
| [NCT01018381](https://clinicaltrials.gov/study/NCT01018381) | 不適用 | 完成 | 130 | 米糠阿拉伯木聚醣用於肝癌與 B、C 型肝炎；與 entecavir 無直接關係 |
| [NCT01928511](https://clinicaltrials.gov/study/NCT01928511) | Phase 4 | 完成 | 254 | 長期核苷(酸)類藥物治療的 B 肝患者，改用或加上聚乙二醇干擾素；僅以肝炎關鍵字匹配 |
| [NCT02881008](https://clinicaltrials.gov/study/NCT02881008) | Phase 1/2 | 完成 | 48 | Myrcludex B 對比 entecavir 用於 HBeAg 陰性慢性 B 肝；entecavir 為對照組 |
| [NCT00096785](https://clinicaltrials.gov/study/NCT00096785) | Phase 3 | 完成 | 69 | Entecavir 對比 adefovir 用於未治療過的慢性 B 肝 |
| [NCT00065507](https://clinicaltrials.gov/study/NCT00065507) | Phase 3 | 完成 | 195 | Entecavir 對比 adefovir 用於肝功能失代償的 B 肝 |
| [NCT05416008](https://clinicaltrials.gov/study/NCT05416008) | 不適用 | 未知 | 150 | 長期使用核苷(酸)類藥物與肝脂肪變性的觀察性研究 |
| [NCT01354652](https://clinicaltrials.gov/study/NCT01354652) | Phase 4 | 提前終止 | 5 | Entecavir 在重度肝硬化或肝衰竭患者的乳酸中毒發生率 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | 世代研究 | Viruses | 追蹤 66 位抗 HCV 抗體陽性的慢性 B 肝患者，觀察接受核苷(酸)類藥物後 HCV 病毒量與再活化情形 |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | HBV/HCV 共感染治療進展，指出這類患者肝硬化與肝癌風險高、需有效治療 |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Review／病例 | Clin Res Hepatol Gastroenterol | HBV/HCV 共感染肝損傷較重，治療是臨床挑戰 |
| [29194858](https://pubmed.ncbi.nlm.nih.gov/29194858/) | 2018 | 未分類 | J Viral Hepat | 接受 DAA 治療的 C 肝患者，HBV 再活化及後續肝炎的發生率低 |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | 未分類 | J Gastroenterol Hepatol | C 肝合併 HBV 感染者使用 DAA 時的 HBV 再活化風險 |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | 未分類 | Minerva Gastroenterol Dietol | 回顧 B、C 型肝炎抗病毒藥物（含 entecavir）及其對腎功能的影響 |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | 未分類 | Clin Res Hepatol Gastroenterol | 兒童 B、C 型肝炎現況與未來處置 |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | 未分類 | Wien Med Wochenschr | B、C 型肝炎治療現況與展望 |
| [38450508](https://pubmed.ncbi.nlm.nih.gov/38450508/) | 2024 | 未分類 | Rev Esp Enferm Dig | 血友病與肝病：entecavir 與 tenofovir 使 B 肝可有效治療，C 肝則靠 DAA |
| [28487602](https://pubmed.ncbi.nlm.nih.gov/28487602/) | 2017 | 未分類 | World J Gastroenterol | B 肝與酒精性肝病成為肝癌主因的趨勢；C 肝已可由 DAA 根除 |

這些文獻都沒有顯示 entecavir 本身能治療 C 型肝炎。

## 香港上市資訊

共 20 張許可證，以下列出 5 張主要許可證。資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-65737 | ENTECAVIR LEK SANDOZ TABLETS 0.5MG | SANDOZ HONG KONG LIMITED |
| HK-64435 | PMS-ENTECAVIR TABLETS 0.5MG | TRENTON-BOMA LTD |
| HK-68822 | ENTECAVIR TEVA TABLETS 0.5MG | TEVA PHARMACEUTICAL HONG KONG LIMITED |
| HK-66332 | ENTIGIN TABLETS 0.5MG | YUNG SHIN CO LTD |
| HK-55152 | BARACLUDE TAB 0.5MG | BRISTOL-MYERS SQUIBB PHARMA (HK) LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何試驗或文獻顯示 entecavir 對 C 型肝炎有直接療效，機轉上也沒有 HCV 靶點，模型高分應是網絡關聯造成。
- 只有 HBV/HCV 共感染時 entecavir 才有臨床角色，處理的是 B 肝部分，屬於既有用途，不算 C 肝的新適應症。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌資料。
- 補充 DrugBank 的作用機轉資料。
- 做體外抗 HCV 活性試驗，確認 entecavir 是否有直接作用。
- 若以共感染為方向，改為評估 HBV 再活化預防的定位，並重新定義適應症。

**補充觀察：** 同一份預測清單中，「B 型肝炎病毒感染」（第 2 名）是既有適應症，可視為驗證模型的正向對照，證據等級 L1。「HIV 感染」（第 3 名）有真實的抗 HIV 逆轉錄酶活性，但可能選出 M184V 抗藥突變，需另行評估安全性。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

