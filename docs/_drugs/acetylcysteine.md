---
layout: default
title: Acetylcysteine
parent: 高證據等級 (L1-L2)
nav_order: 20
evidence_level: L2
indication_count: 10
---

# Acetylcysteine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Acetylcysteine：從支氣管炎與對乙醯胺酚中毒到血栓性疾病

## 一句話總結

Acetylcysteine（N-乙醯半胱胺酸，NAC）是一種黏液溶解劑與抗氧化劑，原本用於支氣管炎、對乙醯胺酚（paracetamol）中毒、囊狀纖維化等適應症。
TxGNN 模型預測它可能對**血栓性疾病 (Thrombotic Disease)** 有效，目前有 **7 個臨床試驗**和 **20 篇文獻**支持這個方向。不過，訊號主要集中在血栓性微血管病（TMA/TTP），不是一般血栓。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 支氣管炎、對乙醯胺酚中毒、囊狀纖維化、支氣管擴張、類澱粉沉積症（來自知識圖譜；香港許可證未載明核准適應症文字） |
| 預測新適應症 | 血栓性疾病 (Thrombotic Disease) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold（列為研究問題，待確認試驗結果） |

---

## 為什麼這個預測合理？

NAC 是含硫醇（thiol）的分子，可還原超大型血管性血友病因子（VWF）多聚體中的雙硫鍵，降低 VWF 與血小板的結合，進而減少微血栓形成。小鼠與狒狒的 TTP 前臨床模型支持這個機制。此外，NAC 的抗氧化作用可能減輕內皮細胞損傷，與移植相關血栓性微血管病（TA-TMA）的病理有關。

目前缺乏詳細的作用機轉資料庫記錄（DrugBank MOA 欄位無資料），以上機轉說明來自本報告所整理的文獻與前臨床研究。

需要留意的是：目前訊號最強的是 TMA/TTP 類疾病，並非泛指所有血栓性疾病。原適應症（呼吸道黏液、解毒）與血栓性疾病在臨床上關聯有限，這個預測更像是由「硫醇還原雙硫鍵＋抗氧化」的機轉推導出來的。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Phase 3 | 完成 | 170 | NAC 用於移植相關血栓性微血管病（TA-TMA）的安全性與療效；結果未公開 |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Phase 2/3 | 進行中（不再招募） | 44 | 單臂多中心試驗，NAC 治療 TA-TMA；尚無結果 |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Phase 2 | 完成 | 40 | RENACTIF：雙盲、安慰劑對照、交叉試驗，NAC 降低腎功能不全患者的血栓傾向 |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Early Phase 1 | 完成 | 3 | 疑似 TTP 併用血漿置換的先導試驗，樣本過小 |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Phase 2 | 未知 | 44 | 高劑量 dexamethasone 併用 NAC 治療新診斷免疫性血小板低下症（ITP）；與血栓僅間接相關 |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Early Phase 1 | 完成 | 15 | Atorvastatin 併用 NAC 對 ITP 血小板數的影響；間接相關 |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Phase 1/2 | 未知 | 200 | Atorvastatin、NAC 與 danazol 併用治療類固醇抗藥或復發 ITP；NAC 的效果被併用藥混淆 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41977015](https://pubmed.ncbi.nlm.nih.gov/41977015/) | 2026 | 系統性回顧 | J Clin Med | NAC 用於 TTP 的系統性回顧與批判性評讀 |
| [42338865](https://pubmed.ncbi.nlm.nih.gov/42338865/) | 2026 | 系統性回顧 | Cureus | NAC 作為 TTP 輔助治療的系統性回顧 |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | 世代研究 | Ann Hematol | 回溯性研究，探討 NAC 與後天性 TTP 院內死亡率的關聯；NAC 在此用途仍有爭議 |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Review | Blood | TTP 的病理機轉與治療回顧 |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Review | J Clin Med | TTP 的病理生理、診斷與處置 |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Review | Expert Rev Hematol | TTP 的新興與再利用藥物，包括 NAC |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | 前臨床（小鼠/狒狒） | Blood | NAC 在 TTP 動物模型中的研究，為雙硫鍵還原機轉提供支持 |
| [36410267](https://pubmed.ncbi.nlm.nih.gov/36410267/) | 2022 | Review | J Infect Public Health | NAC 用於 COVID-19（含高凝狀態）的證據回顧 |
| [28645643](https://pubmed.ncbi.nlm.nih.gov/28645643/) | 2017 | Review | Transfus Clin Biol | TTP 處置回顧 |
| [32614622](https://pubmed.ncbi.nlm.nih.gov/32614622/) | 2021 | Review | Platelets | 針對 VWF 與 GPIb 的新型抗血小板策略 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63073 | ADVANCE MUCOLYTIC POWDER 200MG/SACHET | 未載明 | 未載明 |
| HK-52560 | ACTEIN GRANULES 100MG | 未載明 | 未載明 |
| HK-65198 | AZEIN CAPSULES 200MG | 未載明 | 未載明 |
| HK-54293 | MICOSTEINE POWDER FOR ORAL SUSP 200MG/SACHET | 未載明 | 未載明 |
| HK-42254 | FLUIMUCIL INJ 300MG/3ML | 未載明 | 未載明 |

以上僅列出 5 張，共 20 張有效單方許可證，全部為有效狀態，無已註銷者。

---

## 安全性考量

- **知識圖譜所列相關疾病（非仿單文字）**：消化性潰瘍、低血壓、呼吸衰竭、氣喘、支氣管疾病、食道靜脈曲張。
- **藥物交互作用**：資料庫共記錄 100 筆。其中 Activated charcoal 為輕度；人類吸入型速效胰島素（Insulin human, inhalation）為中度；其餘多數等級未明，例如 Metformin、Omeprazole、Pantoprazole、Morphine、Prednisone 等。

其餘警語與禁忌資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（列為研究問題）**

**理由：**
- 雖有 1 個已完成的 Phase 3（NCT03252925），但結果未公開，無法確認療效，證據暫定為 L2。其餘多為小型、間接或與其他藥物併用的試驗。
- 目前最有力的訊號是 TA-TMA 與 TTP，不適合直接延伸到泛稱的「血栓性疾病」。香港許可證也沒有相關核准適應症。

**若要推進需要：**
- 取得 NCT03252925 與 NCT07279610 的結果，確認療效與安全性。
- 把目標適應症縮窄為 TA-TMA 或 TTP，而非泛稱血栓性疾病。
- 補齊作用機轉資料與香港仿單的警語與禁忌。
- 評估 NAC 對血栓或出血風險的影響，以及與抗凝血、抗血小板藥物併用的安全性。

---

## 其他預測適應症簡述

| 預測適應症 | 分數 | 證據等級 | 建議 | 備註 |
|-----------|------|---------|------|------|
| 乾眼症 (Dry Eye Syndrome) | 99.87% | L2 | Proceed with Guardrails | 有 chitosan-NAC 滴眼液的 Phase 1/2 試驗與隨機對照研究；Sjögren 乾燥症狀的隨機安慰劑對照研究（PMID 39360368）。證據比首要預測更完整，建議優先評估。 |
| 氣管疾病 | 99.57% | L4 | Research Question | 僅有體外與動物研究，且與既有支氣管炎、囊狀纖維化用途重疊。 |
| 鼻腔疾病 | 99.92% | L4 | Hold | 文獻間接，無臨床試驗。 |
| 咽炎 | 99.80% | L4 | Hold | 僅有與抗生素併用的兒童研究，無法區分 NAC 的貢獻。 |
| 短暫性腦缺血發作 | 99.53% | L4 | Hold | 僅有動物研究。 |
| 閉角型青光眼、急性喉咽炎、喉氣管炎、隅角閉鎖性青光眼 | 99.31%–99.95% | L5 | Hold | 僅有模型預測，無試驗或文獻；兩個青光眼條目可能為同義詞，應合併檢視。 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

