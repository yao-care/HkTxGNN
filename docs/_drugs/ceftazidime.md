---
layout: default
title: Ceftazidime
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Ceftazidime
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Ceftazidime：從細菌感染到泌尿道感染（尿路感染）

## 一句話總結

Ceftazidime 是第三代頭孢菌素類抗生素，原本用於鏈球菌感染、細菌性肺炎、細菌性腦膜炎、腹膜炎等多種細菌感染。
TxGNN 模型預測分數最高的是高澱粉酶血症，但該預測缺乏機轉與臨床支持。證據較完整的方向是**泌尿道感染 (Urinary Tract Infection)**，目前有 **4 個臨床試驗**和 **20 篇文獻**，不過其中多數涉及 ceftazidime-avibactam 複方，且泌尿道感染與原適應症性質接近，較像核准適應症的延伸，而非真正的再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌感染類疾病（鏈球菌感染、細菌性肺炎、腦膜炎、腹膜炎等） |
| 預測新適應症 | 高澱粉酶血症 (Hyperamylasemia)（排名第 1，無證據支持）；證據最完整的為泌尿道感染 (rank 4) |
| TxGNN 預測分數 | 高澱粉酶血症 99.51%；泌尿道感染 99.41% |
| 證據等級 | 高澱粉酶血症 L5；泌尿道感染 L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | 高澱粉酶血症 Hold；泌尿道感染 Proceed with Guardrails |

> 說明：排名第 1 的預測缺乏證據，因此以下證據章節改以證據最完整的泌尿道感染為主。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ceftazidime 屬於第三代頭孢菌素，透過抑制青黴素結合蛋白 (PBP)，干擾細菌細胞壁合成而殺菌。對革蘭氏陰性菌（包括綠膿桿菌與腸內菌科）有廣泛活性。

這個機轉與複雜性泌尿道感染的致病菌高度重疊，所以泌尿道感染的預測在生物學上合理。不過，原適應症本身已包含多種細菌感染，泌尿道感染更適合視為核准範圍內或接近核准範圍的使用，而非典型的藥物再利用。此外，多數新近證據來自 ceftazidime-avibactam 複方，不能完全歸因於 ceftazidime 單方。

其他預測的合理性差異很大：
- **高澱粉酶血症、多株性高黏滯症候群、先天性無白蛋白血症、血型不合**：均為生化、血液或免疫問題，與抗菌機轉無關，應視為圖譜預測的假象。
- **Ureaplasma 尿道炎**：Ureaplasma 沒有細胞壁，β-內醯胺類在機轉上無效。
- **淋病性尿道炎**：頭孢菌素對淋病雙球菌有活性，但標準選擇是 ceftriaxone，且無支持證據。
- **會厭炎、Peptostreptococcus 感染**：僅有個案報告或 1981 年體外試驗，不足以支持臨床使用。
- **感染性中耳炎**：主要針對慢性化膿性中耳炎（綠膿桿菌常見），有數項兒童研究，但多為舊的小型非隨機研究。

---

## 臨床試驗證據

（針對泌尿道感染）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00921024](https://clinicaltrials.gov/study/NCT00921024) | Phase 2 | 完成 | 129 | 雙盲隨機試驗，比較靜脈 CXA-101 與 ceftazidime 用於複雜性泌尿道感染（含腎盂腎炎） |
| [NCT04882085](https://clinicaltrials.gov/study/NCT04882085) | Phase 4 | 完成 | 60 | 開放標籤隨機試驗，比較 ceftazidime-avibactam 與最佳可用治療，用於中國成人碳青黴烯類抗藥性革蘭氏陰性菌感染（含 cUTI） |
| [NCT01430910](https://clinicaltrials.gov/study/NCT01430910) | Phase 1 | 完成 | 43 | ceftazidime-avibactam 在健康受試者的藥動學與藥物交互作用研究，非療效試驗 |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | 不適用 | 招募中 | 5000 | 兒童與青年「研究不足藥物」的藥動學、藥效學與安全性研究，並非針對 ceftazidime 或泌尿道感染 |

---

## 文獻證據

（泌尿道感染相關，優先列出較相關者）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32094128](https://pubmed.ncbi.nlm.nih.gov/32094128/) | 2020 | 多中心回溯性世代研究（資料庫標註為 RCT，實為回溯研究） | Antimicrob Agents Chemother | 比較 meropenem-vaborbactam 與 ceftazidime-avibactam 治療碳青黴烯類抗藥性腸內菌科感染 |
| [30270406](https://pubmed.ncbi.nlm.nih.gov/30270406/) | 2018 | RCT (Phase 3) | Infect Dis Ther | TANGO II：meropenem-vaborbactam 對比最佳可用治療，用於 CRE 感染 |
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | 系統性回顧與網絡統合分析 | J Comp Eff Res | 評估複雜性泌尿道感染與急性腎盂腎炎的治療選項療效 |
| [38688353](https://pubmed.ncbi.nlm.nih.gov/38688353/) | 2024 | Review | Int J Antimicrob Agents | 義大利與法國感染症學會的多重抗藥性革蘭氏陰性菌治療實務建議 |
| [35787918](https://pubmed.ncbi.nlm.nih.gov/35787918/) | 2022 | Review | Int J Antimicrob Agents | 新型抗生素治療多重抗藥性革蘭氏陰性菌的臨床資料，支持 ceftazidime-avibactam 等組合 |
| [30219824](https://pubmed.ncbi.nlm.nih.gov/30219824/) | 2019 | Review | Clin Infect Dis | 抗生素腎功能劑量調整，討論 ceftazidime/avibactam 在肌酸酐清除率 30–50 mL/min 病人的反應 |
| [33618353](https://pubmed.ncbi.nlm.nih.gov/33618353/) | 2021 | 回溯性觀察多中心研究 | Clin Infect Dis | ceftazidime-avibactam 用於 KPC 型肺炎克雷伯菌感染 |
| [39934901](https://pubmed.ncbi.nlm.nih.gov/39934901/) | 2025 | 系統性回顧與統合分析 | Antimicrob Resist Infect Control | 全球革蘭氏陰性菌對 ceftazidime-avibactam 的抗藥性趨勢 |
| [26289307](https://pubmed.ncbi.nlm.nih.gov/26289307/) | 2015 | Review | Pharmacotherapy | ceftazidime-avibactam 的藥理與臨床回顧 |
| [30224941](https://pubmed.ncbi.nlm.nih.gov/30224941/) | 2018 | 研究 | Can J Infect Dis Med Microbiol | 導尿管相關泌尿道感染與生物膜形成菌 |

另有針對慢性化膿性中耳炎的兒童研究（例如 [10826908](https://pubmed.ncbi.nlm.nih.gov/10826908/)，2000 年，ceftazidime 與 aztreonam 比較，每組 15 名兒童，開放隨機試驗），可作為該適應症的研究線索，但屬於舊的小型研究。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-21523 | FORTUM FOR INJ 2G | 注射劑 | 請參考仿單 |
| HK-21522 | FORTUM FOR INJ 500MG | 注射劑 | 請參考仿單 |
| HK-57297 | CEFTAZIDIME FOR INJ 1G (REYOUNG) | 注射劑 | 請參考仿單 |
| HK-61251 | CEFTAZIDIME POWDER FOR SOLUTION FOR INJECTION 2G | 注射劑 | 請參考仿單 |
| HK-21251 | FORTUM FOR INJ 1G | 注射劑 | 請參考仿單 |

另有 3 張有效許可證（HK-61252、HK-61250 及 ZAVICEFTA HK-66061，後者為 ceftazidime/avibactam 製劑），共 8 張有效單一成分許可證。

---

## 安全性考量

- **知識圖譜標示的相關疾病禁忌**：腎臟疾病、輸尿管積膿、肝臟疾病、膽囊疾病、凝血功能疾病、困難梭狀芽孢桿菌結腸炎、新生兒壞死性腸炎、先天性凝血酶原缺乏。（此為知識圖譜關聯，並非仿單文字。）
- **藥物交互作用**（共查得 100 筆，以下為中度者）：Amphotericin B（含各種劑型）、Kanamycin、Neomycin、Streptomycin、Picosulfuric acid。
- 其餘多為等級未知，例如 Calcitriol、Pantoprazole、Doxycycline、Morphine、Metformin、Omeprazole、Vancomycin 等。

仿單警語與禁忌的詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：**
- 高澱粉酶血症（排名第 1）：**Hold**
- 泌尿道感染：**Proceed with Guardrails**

**理由：**
- 排名最高的幾項預測（高澱粉酶血症、多株性高黏滯症候群、先天性無白蛋白血症、血型不合）沒有機轉或臨床支持，應視為模型假象。
- 泌尿道感染有 Phase 2 隨機雙盲試驗與多篇文獻，機轉合理，但它接近核准範圍，且證據多來自 ceftazidime-avibactam 複方。

**若要推進需要：**
- 取得香港仿單的核准適應症、警語與禁忌，確認泌尿道感染是否已在核准範圍內
- 補齊作用機轉資料
- 釐清 NCT00921024 的確切比較組合，並區分 ceftazidime 單方與複方的證據
- 針對抗藥性（ESBL、碳青黴烯酶產生菌）與腎功能劑量調整建立監測與用藥指引
- 慢性化膿性中耳炎方向可列為研究問題，需更新、更嚴謹的臨床資料
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

