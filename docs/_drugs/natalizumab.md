---
layout: default
title: Natalizumab
parent: 僅模型預測 (L5)
nav_order: 515
evidence_level: L5
indication_count: 5
---

# Natalizumab
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

# Natalizumab：多重適應症再利用評估（首選預測：支氣管炎，最具證據候選：乾癬）

## 一句話總結

Natalizumab 是抗 α4-integrin (VLA-4) 單株抗體，其原適應症在本評估的結構化資料中缺失（僅由文獻脈絡得知曾用於 relapsing-remitting multiple sclerosis）。TxGNN 對本藥共產生 **5 個新適應症預測**，分數最高者為**支氣管炎 (Bronchitis)**，但該預測**無任何機轉或文獻證據支持**；證據量最豐富的是**乾癬 (Psoriasis)**（19 篇文獻），但方向多為「natalizumab 誘發/惡化乾癬」的不良反應通報，而非治療性訊號。5 項預測的系統建議均為 **Hold**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（`original_indications` 為空；文獻脈絡顯示用於 relapsing-remitting multiple sclerosis，非結構化正式記錄） |
| 預測新適應症（TxGNN 分數最高） | 支氣管炎 Bronchitis（rank 1） |
| TxGNN 預測分數 | 99.46%（bronchitis）；其餘 4 項介於 99.04%–99.37% |
| 證據等級 | L5（bronchitis 無任何證據；5 項中最高為 L4，見乾癬/類乾癬/急性苔蘚樣糠疹） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（`original_moa` 為 Data Gap）。根據 5 項預測各自的 `repurposing_rationale`，情況並不一致：

**分數最高的支氣管炎預測本身不合理**：evidence pack 明確指出「natalizumab 為高度組織選擇性（中樞神經/腸道）之 α4-integrin 抗體，與支氣管炎之呼吸道發炎病理無已知直接連結」，且無任何臨床試驗或文獻佐證，判定為 TxGNN 知識圖譜的間接關聯雜訊。

**證據量最大但方向矛盾的是乾癬**：Natalizumab 阻斷白血球經 VCAM-1/MAdCAM-1 之黏附與遷移，理論上與 anti-LFA-1 藥物（efalizumab，已知可治乾癬）機轉類似。但實際 19 篇文獻中，多數（case report）記載的是 natalizumab **誘發或惡化**乾癬（含膿疱型），僅 1 篇小型病例系列（PMID 33589543）觀察到合併症乾癬病人症狀改善。整體證據方向以不良反應通報為主，非治療性訊號。

**類乾癬與急性苔蘚樣糠疹**兩項預測共享同一篇個案報告（PMID 32470781），內容為 natalizumab 治療 MS 期間出現的非預期皮膚不良反應，同樣屬致病而非治療證據。

**嚴重非增殖性糖尿病視網膜病變**僅有機轉推論（VLA-4/VCAM-1 路徑參與白血球滯留），無任何臨床或文獻資料。

---

## 各預測適應症之臨床試驗證據

5 項預測的 `clinical_trials` 與 `ictrp_trials` 皆為空：**目前無相關臨床試驗登記**。

---

## 文獻證據（以乾癬為主，證據量最豐富者）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33589543](https://pubmed.ncbi.nlm.nih.gov/33589543/) | 2021 | Cohort | Neurol Neuroimmunol Neuroinflamm | 18 名 MS 合併乾癬病人使用 natalizumab，觀察到合併症乾癬症狀改善 |
| [30323758](https://pubmed.ncbi.nlm.nih.gov/30323758/) | 2018 | Case Report | Case Rep Neurol | 33 歲病人於 natalizumab 治療期間出現斑塊型乾癬 |
| [23096069](https://pubmed.ncbi.nlm.nih.gov/23096069/) | 2012 | Case Report | J Neurol | natalizumab 治療期間乾癬嚴重惡化並轉為抗藥性病程 |
| [35646438](https://pubmed.ncbi.nlm.nih.gov/35646438/) | 2022 | Case Report | Dermatol Pract Concept | natalizumab 誘發之掌蹠膿疱型乾癬 |
| [28905124](https://pubmed.ncbi.nlm.nih.gov/28905124/) | 2018 | Case Report | Neurol Sci | natalizumab 治療期間出現關節病性乾癬個案報告與文獻回顧 |
| [40526577](https://pubmed.ncbi.nlm.nih.gov/40526577/) | 2025 | Review | Dtsch Arztebl Int | MS 合併慢性發炎疾病（含乾癬）之治療選項回顧 |
| [28765121](https://pubmed.ncbi.nlm.nih.gov/28765121/) | 2018 | Review | Ann Rheum Dis | 免疫調節新療法於類風濕性關節炎、乾癬等疾病之應用回顧 |
| [15955735](https://pubmed.ncbi.nlm.nih.gov/15955735/) | 2005 | Review | Curr Opin Pharmacol | 抗黏附療法（integrin 標的藥物）機轉回顧 |
| [19184539](https://pubmed.ncbi.nlm.nih.gov/19184539/) | 2009 | Review | Immunol Res | 白血球 integrin 及其配體交互作用；integrin 拮抗劑於乾癬與 MS 之治療潛力 |
| [25448040](https://pubmed.ncbi.nlm.nih.gov/25448040/) | 2015 | Review | Pharmacol Ther | 白血球 integrin 於發炎疾病中的角色與治療標的 |

**類乾癬 (Parapsoriasis) 與急性苔蘚樣糠疹**：僅各 1 篇文獻，均為同一篇個案報告 [32470781](https://pubmed.ncbi.nlm.nih.gov/32470781/)（2020，Case Report，Clin Neurol Neurosurg）——描述 fingolimod 與 natalizumab 治療 MS 期間出現的非預期皮膚不良反應，屬藥物誘發之皮膚病變記錄，非治療證據。

**支氣管炎、嚴重非增殖性糖尿病視網膜病變**：目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 注意：本評估存在一項 **Blocking 等級資料缺口**（DG001：TFDA 仿單警語/禁忌未取得），已導致無法進入 S1 安全性初評；`key_warnings`、`contraindications`、DDI 查詢均無資料（`ddi.query_status = not_found`）。Natalizumab 已知具進行性多灶性白質腦病（PML）風險，此為文獻中反覆出現的背景資訊，但未在本次結構化安全性欄位中取得正式仿單佐證，不應作為結論依據。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 5 項預測建議欄位（`scoring.recommendation`）均為 Hold，無一達到 S1 以上決策階段。
- 分數最高的支氣管炎預測缺乏任何機轉或實證支持，屬 KG 雜訊訊號。
- 證據量最大的乾癬預測方向矛盾——多數證據顯示 natalizumab **誘發/惡化**乾癬，僅 1 篇小型世代研究提示可能益處，不足以支持治療性再利用。
- 安全性評估因 DG001（Blocking）無法完成，藥物本身在香港未上市，無許可證資料可佐證在地可及性。

**若要推進需要：**
- 取得 TFDA/藥監局官方仿單，完成警語與禁忌之 S1 安全性初評（DG001，Blocking）。
- 補齊 DrugBank MOA 完整資料，以強化機轉關聯性分析（DG002，High）。
- 若欲深入乾癬方向，需針對合併症族群設計前瞻性研究，釐清 33589543 觀察到的改善是否為真實治療訊號，或僅為病人選擇偏差。
- 支氣管炎、嚴重非增殖性糖尿病視網膜病變兩項預測目前無實證基礎，建議暫緩投入資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

