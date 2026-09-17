---
layout: default
title: Telbivudine
parent: 中證據等級 (L3-L4)
nav_order: 724
evidence_level: L4
indication_count: 5
---

# Telbivudine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# TELBIVUDINE：從慢性B型肝炎到慢性C型肝炎感染（證據不支持此預測）

## 一句話總結

Telbivudine（DB01265）是專一性抗 B 型肝炎病毒（HBV）核苷類似物，目前未在香港上市。TxGNN 模型將**慢性C型肝炎病毒感染 (Chronic HCV Infection)** 列為第一預測適應症（分數 99.96%），但證據集內附的機轉分析已明確指出此為模型假陽性——所列臨床試驗與文獻實質上全數是 HBV 相關研究，並非針對 HCV 的 telbivudine 試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無許可證資料（本藥未在香港上市；drug.original_indications 亦為空）。根據證據集內機轉描述，telbivudine 原始設計標的為慢性B型肝炎 |
| 預測新適應症 | 慢性C型肝炎病毒感染 (Chronic Hepatitis C Virus Infection) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold** |

## 為什麼這個預測不合理

證據集本身已對此預測提出明確反證，而非單純缺乏資料：

**機轉層面不支持。** HCV 為 RNA 病毒，複製依賴 NS5B RNA 依賴性 RNA 聚合酶；telbivudine 的標的是 HBV DNA 聚合酶（反轉錄酶），兩者結構與作用機制不同，目前無任何已知交叉抑制證據。

**所列「證據」實質上與 HCV 無關。** 檢視 evidence.clinical_trials 中的試驗，多數（如 NCT01925820、NCT00142298、NCT02058108）研究對象皆為 HBV（慢性B型肝炎）病人，並非 HCV 感染者；telbivudine 的機轉關聯性分析也指出，這是 TxGNN 因 HBV/HCV 常在「病毒性肝炎」文獻中共同出現、導致疾病嵌入向量相似度偏高所產生的**假陽性**，而非真實的藥理學關聯。

**佐證資料同樣支持這個結論**：本證據集第 2 名預測「hepatitis B virus infection」才是 telbivudine 真正具機轉基礎、且有 L1 等級證據（多個 Phase 3 RCT）支持的適應症——但這實質上是藥物的**原始設計適應症**而非新用途；第 3 名「HIV infectious disease」已被文獻（PMID 22024528、20308377）直接證實體外與人體均無抗 HIV-1 活性；第 5 名「苯丙胺酸代謝異常」則完全無機轉關聯、零試驗、零文獻支持。整體而言，本批次 TxGNN 預測中**沒有發現具備機轉合理性的新適應症候選**。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00805675](https://clinicaltrials.gov/study/NCT00805675) | Phase 3 | 完成 | 83 | Telbivudine+Tenofovir 治療 HBeAg 陽性 CHB 之病毒動力學比較，**非 HCV 研究** |
| [NCT01925820](https://clinicaltrials.gov/study/NCT01925820) | Phase 4 | 未知 | 540 | 研究藥物為 Pegasys/Entecavir，疾病為 HBeAg 陰性 CHB，與 telbivudine 及 HCV 皆無關（評為 C 級） |
| [NCT00142298](https://clinicaltrials.gov/study/NCT00142298) | Phase 3 | 完成 | 1869 | Telbivudine 於慢性 B 型肝炎病人之延伸試驗，非 HCV（評為 C 級） |
| [NCT03181607](https://clinicaltrials.gov/study/NCT03181607) | N/A | 未知 | 300 | TDF/Telbivudine 用於預防 HBV 母嬰垂直傳染，非 HCV |
| [NCT00412529](https://clinicaltrials.gov/study/NCT00412529) | Phase 3 | 完成 | 44 | Telbivudine vs Entecavir 於 HBeAg 陽性 CHB 之病毒動力學，非 HCV |
| [NCT00810524](https://clinicaltrials.gov/study/NCT00810524) | Phase 4 | 未知 | 600 | 慢性 HBV 感染抗病毒治療對長期預後之影響，非 HCV |
| [NCT02956850](https://clinicaltrials.gov/study/NCT02956850) | Phase 1 | 完成 | 160 | RO7020531（非 telbivudine）於慢性 HBV 病人之安全性研究 |
| [NCT02058108](https://clinicaltrials.gov/study/NCT02058108) | Phase 3 | 終止 | 53 | Telbivudine 於兒童/青少年 CHB 病人之研究，非 HCV，且已終止（評為 C 級） |
| [NCT01083251](https://clinicaltrials.gov/study/NCT01083251) | N/A | 未知 | 120 | 維生素D輔助 Peg-IFN 或 telbivudine 治療慢性 HBV 感染，非 HCV |
| [NCT05466071](https://clinicaltrials.gov/study/NCT05466071) | N/A | 未知 | 200 | Tenofovir alafenamide 預防 HBV 母嬰垂直傳染，非 telbivudine 亦非 HCV |

**結論：以上 10 個試驗中無一為針對 HCV 感染設計、且使用 telbivudine 作為研究藥物的試驗。**

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | HBV 與 HCV 治療現況綜述，僅並列討論兩種疾病，非 telbivudine 抗 HCV 證據 |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | 綜述 HBV/HCV 抗病毒藥物對腎功能影響，telbivudine 僅列於 HBV 藥物分類 |
| [28845882](https://pubmed.ncbi.nlm.nih.gov/28845882/) | 2018 | pending | J Viral Hepat | 探討 HCV 直接抗病毒藥物（DAA）治療期間 HBV 再活化風險，與 telbivudine 治 HCV 無關 |
| [19344237](https://pubmed.ncbi.nlm.nih.gov/19344237/) | 2009 | Review | Expert Rev Anti Infect Ther | 慢性 B、C 型肝炎治療管理觀點綜述，無摘要內容 |
| [25233195](https://pubmed.ncbi.nlm.nih.gov/25233195/) | 2014 | pending | J Perinatol | 妊娠期 HBV/HCV 感染綜述，聚焦母嬰垂直傳染，非 telbivudine 抗 HCV 資料 |
| [18330099](https://pubmed.ncbi.nlm.nih.gov/18330099/) | 2007 | pending | Acta Gastroenterol Belg | 比利時 HBV 管理指引，無摘要 |
| [18340426](https://pubmed.ncbi.nlm.nih.gov/18340426/) | 2008 | pending | Der Internist | 德國 HBV/HCV 治療建議更新，telbivudine 僅列為 HBV 單一療法選項 |
| [23697556](https://pubmed.ncbi.nlm.nih.gov/23697556/) | 2013 | pending | J Interferon Cytokine Res | Telbivudine 治療慢性 HBV 病人之 IL-37 血清濃度研究，非 HCV |
| [21964179](https://pubmed.ncbi.nlm.nih.gov/21964179/) | 2011 | pending | Mayo Clin Proc | 非 HIV 病毒之抗病毒藥物綜述，涵蓋疱疹、肝炎、流感病毒，未特指 telbivudine 對 HCV 之作用 |
| [21999649](https://pubmed.ncbi.nlm.nih.gov/21999649/) | 2011 | pending | Paediatr Drugs | 兒童慢性肝病管理，一般性綜述，非 telbivudine 抗 HCV 直接證據 |

**結論：所有文獻均為 HBV/HCV 並列討論之綜述性質，無任何一篇提供 telbivudine 對 HCV 具療效的直接實驗或臨床證據。**

## 香港上市資訊

本藥目前**未在香港上市**（`market_status: 未上市`），無許可證登記資料（`total_licenses: 0`），故無法列出許可證表格。

## 安全性考量

安全性資訊請參考原廠仿單。（本評估之 key_warnings、contraindications、DDI 查詢均無資料）

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉上不支持：telbivudine 標的為 HBV DNA 聚合酶，HCV 複製依賴完全不同的 RNA 聚合酶系統，無交叉作用基礎。
- 所有列出的臨床試驗與文獻經逐一檢視後，均為 HBV 相關研究，非針對 HCV 的 telbivudine 試驗，證據集本身的機轉分析已將此列為 TxGNN 疾病嵌入相似度導致的假陽性預測。
- 本藥未在香港上市，即使假設此適應症成立，仍需完整的上市與安全性評估路徑。

**若要推進需要（不建議推進，除非有以下實質新證據）：**
- 直接測試 telbivudine 對 HCV NS5B 聚合酶或 HCV 複製子系統的體外抑制活性數據（目前完全缺乏）
- 任何以 HCV 感染者為對象、實際給藥 telbivudine 的臨床試驗結果
- 若上述證據不存在，建議將此適應症從候選清單中移除，並將評估資源轉向本證據集第 2 名「HBV 感染」（L1 證據等級，但屬原始適應症而非新用途）或其他候選藥物。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

