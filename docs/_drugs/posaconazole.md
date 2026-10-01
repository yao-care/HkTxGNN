---
layout: default
title: Posaconazole
parent: 僅模型預測 (L5)
nav_order: 700
evidence_level: L5
indication_count: 1
---

# Posaconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Posaconazole：從抗黴菌用藥到肺囊蟲病

## 一句話總結

Posaconazole 是三唑類（azole）抗黴菌藥，香港已有上市許可證。
TxGNN 模型預測它可能對**肺囊蟲病 (Pneumocystosis)** 有效，但沒有任何臨床試驗或文獻直接支持。
目前有 **2 個間接相關的臨床試驗**（相關度皆為 C 級）和 **5 篇背景文獻**，建議暫緩（Hold）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症 |
| 預測新適應症 | 肺囊蟲病 (Pneumocystosis) |
| TxGNN 預測分數 | 99.77%（排名第 5105） |
| 證據等級 | L4（無直接研究，詳見下文） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 posaconazole 的作用機轉登錄資料。依一般藥理知識，它抑制黴菌的 CYP51（羊毛固醇 14-α-去甲基酶），使麥角固醇（ergosterol）耗竭，進而抑制黴菌生長。

TxGNN 給出 99.77% 的高分，較可能是因為知識圖譜中「azole 類抗黴菌藥」與「黴菌感染」距離很近，而不是模型找到了針對肺囊蟲的作用路徑。

這個預測在機轉上**很弱，甚至可能互相矛盾**：
- 肺囊蟲 (*Pneumocystis jirovecii*) 的細胞膜麥角固醇含量很低，主要使用膽固醇類固醇。
- Azole 類藥物一般不被認為對它有效。
- 標準預防與治療是 trimethoprim-sulfamethoxazole。

因此，高預測分數不能視為療效證據。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | 進行中（已停止收案） | 602 | Rezafungin 對比標準抗微生物方案，用於異體血液與骨髓移植成人的侵襲性黴菌病預防。Posaconazole 至多出現在對照組標準方案中，未評估其對肺囊蟲病的療效。 |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | 招募中 | 358 | 不相合非親緣周邊血幹細胞移植，比較以移植後環磷醯胺為基礎的 GVHD 預防組合。Posaconazole 至多是背景支持性抗感染用藥，與本適應症僅偶然相關。 |

兩個試驗的相關度都是 C 級，**沒有任何一個直接檢驗 posaconazole 對肺囊蟲病的效果**。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Review | The Lancet Infectious Diseases | 英國醫學黴菌學會更新嚴重黴菌病診斷建議，說明非培養法（抗原、抗體、分子檢測）已成診斷主流。 |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | 概述念珠菌、麴菌、隱球菌與肺囊蟲肺炎等侵襲性黴菌病。高風險血液腫瘤病人使用對黴菌有效的 posaconazole 預防，使部分侵襲性黴菌感染明顯減少。 |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Review | 中華結核和呼吸雜誌 | 中國胸腔學會 2025 版侵襲性肺部黴菌病診治指引，特別針對非免疫抑制病人。 |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | 整理抗黴菌等抗感染藥物在肺上皮襯液 (ELF) 的穿透情形，不同劑型、給藥途徑與藥物間濃度有差異。 |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transplant Infectious Disease | 回顧肝臟移植後急性 GVHD 的感染併發症與抗微生物治療模式，感染是主要死因。 |

這些文獻只提供黴菌感染與移植感染的背景，**沒有一篇顯示 posaconazole 對肺囊蟲病有療效**。

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67802 | POSACON ORAL SUSPENSION 40MG/ML | HIND WING CO LTD |
| HK-56439 | NOXAFIL ORAL SUSP 40MG/ML | MERCK SHARP & DOHME (ASIA) LTD |
| HK-68771 | MOMETAMAX ULTRA EAR DROPS SUSPENSION FOR DOGS（獸用） | MERCK SHARP & DOHME (ASIA) LTD |

三張許可證都未登載劑型與核准適應症。HK-68771 是獸用產品，不適用於人類用藥評估。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但機轉上與已知知識相衝突（肺囊蟲缺乏麥角固醇，azole 不被視為有效）。
- 現有試驗和文獻都沒有直接檢驗 posaconazole 對肺囊蟲病的療效，且已有標準療法 trimethoprim-sulfamethoxazole。

**若要推進需要：**
- 取得香港衛生署的仿單，確認核准適應症、警語與禁忌，這是進入安全性篩選的前提。
- 補齊 posaconazole 的作用機轉資料，例如查詢 DrugBank。
- 搜尋是否有體外（in vitro）、動物模型或臨床資料，直接評估 posaconazole 對 *Pneumocystis* 的活性。
- 若有任何正面訊號，再與標準療法比較其可能角色，例如對 TMP-SMX 不耐受的病人。

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

