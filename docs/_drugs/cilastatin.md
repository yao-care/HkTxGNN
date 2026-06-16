---
layout: default
title: Cilastatin
parent: 中證據等級 (L3-L4)
nav_order: 169
evidence_level: L3
indication_count: 10
---

# Cilastatin
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Cilastatin：從 Imipenem/Cilastatin 複方輔助成分到金黃色葡萄球菌感染

## 一句話總結

Cilastatin 是 Imipenem/Cilastatin 複方的必要輔助成分，藉由抑制腎臟去氫胜肽酶-I（DHP-I）防止 Imipenem 被腎小管代謝失活，確保抗菌藥物維持有效的組織濃度。TxGNN 模型預測它可能對**金黃色葡萄球菌感染（Staphylococcus aureus infection）**有效，目前有 **3 個臨床試驗**和 **20 篇文獻**支持這個方向。需特別注意的是，Cilastatin 本身不具抗菌活性，所有相關療效均來自 Imipenem/Cilastatin 複方的整體表現。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無獨立核可適應症（以 Imipenem/Cilastatin 複方形式用於廣效細菌感染） |
| 預測新適應症 | 金黃色葡萄球菌感染（Staphylococcus aureus infection） |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question |

---

## 為什麼這個預測合理？

Cilastatin 在 Imipenem/Cilastatin 複方中扮演「守門員」的角色。Imipenem 進入腎小管後，若不加以保護，會被 DHP-I 酶快速分解而失效；Cilastatin 專一性抑制這個酶，使 Imipenem 在血液和組織中維持足夠的藥物暴露，進而發揮廣效抗菌作用。目前缺乏 Cilastatin 獨立的詳細作用機轉資料，其抗感染療效均以複方情境呈現。

Imipenem/Cilastatin 複方對甲氧西林敏感金黃色葡萄球菌（MSSA）具有體外及臨床殺菌活性。1986 年一項臨床研究（PMID:3460521）評估 23 名患者（含 11 名 MRSA、12 名 MSSA），涵蓋軟組織、心血管及骨骼感染，顯示複方整體具有抗葡萄球菌療效。然而，對甲氧西林抗藥性金黃色葡萄球菌（MRSA）的療效相對受限——動物試驗（PMID:3378959）顯示 Imipenem 在 MRSA 心內膜炎模型中僅具抑菌效果，Vancomycin 殺菌活性更佳；體外比較研究（PMID:12878512）亦確認 Imipenem/Cilastatin 對 MRSA 系統性感染的療效明顯低於 Vancomycin。

2020 年的案例評述（PMID:33020155）描述了難治性 MRSA 菌血症使用 Imipenem/Cilastatin 合併 Fosfomycin 成功治療的情境，顯示在特定耐藥困境下，此複方具有「救援療法（Salvage therapy）」的應用潛力。TxGNN 的預測可能正是捕捉到這種廣效 β-lactam 複方在金黃色葡萄球菌感染生態中的臨床關聯性，但 Cilastatin 作為獨立藥效學貢獻者的角色尚待釐清。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Phase 4 | 未知 | 60 | Linezolid 單用與合併 Carbapenem（可能含 Imipenem）對抗 MRSA 引起的呼吸器相關肺炎；Cilastatin 為複方成分，非獨立受試藥物，資料狀態不明 |
| [NCT00707239](https://clinicaltrials.gov/study/NCT00707239) | Phase 2 | 提早終止 | 108 | Tigecycline 兩種劑量與 Imipenem/Cilastatin 比較用於醫院獲得性肺炎（HAP）；因招募不足提早終止，結論效力存疑，無法支持獨立適應症 |
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | 完成 | 274 | Imipenem/Cilastatin/Relebactam 對比 Piperacillin/Tazobactam 用於 HABP/VABP；主要終點為 28 天全因死亡率，Imipenem/Cilastatin 作為三重複方成分，非評估 Cilastatin 獨立療效的設計 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | 臨床研究 | Antimicrob Agents Chemother | 23 名患者（11 MRSA、12 MSSA）使用 Imipenem/Cilastatin 治療，MRSA MIC90 為 6.25 mg/L，MSSA MIC90 更低；軟組織、心血管、骨骼感染均有療效記錄 |
| [3378959](https://pubmed.ncbi.nlm.nih.gov/3378959/) | 1988 | 實驗研究 | J Antimicrob Chemother | 兔子 MRSA 主動脈瓣心內膜炎模型顯示 Imipenem 體外僅具抑菌效果（MIC90/MBC90：8/32 mg/L），Vancomycin 殺菌活性更強，提示 Imipenem/Cilastatin 在 MRSA 心內膜炎的療效有限 |
| [8514648](https://pubmed.ncbi.nlm.nih.gov/8514648/) | 1993 | 實驗研究 | J Antimicrob Chemother | 小鼠菌血症模型顯示 Imipenem/Cilastatin 合併 Cefotiam 對 MRSA（含 β-lactamase 及非產酶株）具有協同效果，優於任一單獨使用 |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | 實驗研究 | J Antimicrob Chemother | 36 株 MRSA 臨床分離株中，Vancomycin 合併 Imipenem 對 34 株顯示協同或加成效果；嗜中性球減少小鼠大腿感染模型確認 in vivo 協同活性 |
| [8072190](https://pubmed.ncbi.nlm.nih.gov/8072190/) | 1994 | 臨床研究 | Japanese J Antibiotics | 評估 Arbekacin（ABK）合併 Imipenem/Cilastatin 對 MRSA 感染的療效，聯合療法顯示較低 MIC 值，提供合併用藥的臨床參考 |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | 案例評述 | Antimicrob Agents Chemother | 難治性 MRSA 菌血症使用 Imipenem/Cilastatin 合併 Fosfomycin 成功治療的新穎組合策略；強調在常規治療失敗時，個體化抗菌組合的必要性 |
| [22196394](https://pubmed.ncbi.nlm.nih.gov/22196394/) | 2012 | 回顧文獻 | Int J Antimicrob Agents | 系統回顧 MRSA 毒力策略、嚴重感染治療臨床試驗及抗藥性影響，整合當時最新的 MRSA 治療指引與藥物選擇 |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | 回顧文獻 | Int J Antimicrob Agents | 討論多重抗藥性菌（含 MRSA、VRE 及耐碳青黴烯革蘭氏陰性菌）的仿單核可與非核可使用情況，為 Imipenem/Cilastatin 的延伸應用提供當代框架 |
| [12878512](https://pubmed.ncbi.nlm.nih.gov/12878512/) | 2003 | 實驗研究 | Antimicrob Agents Chemother | 系統性 MRSA 感染模型中，Imipenem/Cilastatin 療效（ED50 >100 mg/kg）明顯低於 Vancomycin（ED50 ~7.21 mg/kg），確認對 MRSA 的相對劣勢 |
| [3890533](https://pubmed.ncbi.nlm.nih.gov/3890533/) | 1985 | 回顧文獻 | Am J Medicine | 早期探討細菌性心內膜炎病理機轉與治療策略，包含 Imipenem 廣效抗菌活性的初步評估及快速殺菌藥物於心內膜炎的重要性論述 |

---

## 香港上市資訊

Cilastatin 目前在香港**無獨立上市許可證記錄**（許可證數：0）。臨床使用均以 Imipenem/Cilastatin 複方形式（如 Tienam®）進行，相關許可證登記於複方藥品名下，而非 Cilastatin 單方。若考慮推進，需以複方形式提交香港衛生署的新適應症申請。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **補充說明**：根據已知文獻，Imipenem/Cilastatin 複方的已知不良反應包含癲癇發作（尤其於腎功能受損患者及高劑量使用）、噁心/嘔吐及注射部位反應。PMID:9158321 記錄一例 Imipenem/Cilastatin 誘發的白血球裂解性血管炎（Leukocytoclastic vasculitis），PMID:26944380 則記錄一例急性嗜酸性球性肺炎。正式安全性評估仍需取得完整仿單資料。

---

## 結論與下一步

**決策：Research Question**

**理由：**
目前有觀察性研究、實驗室證據及個案報告支持 Imipenem/Cilastatin 複方在金黃色葡萄球菌感染（尤其難治性 MRSA）中的潛在應用，但 Cilastatin 本身無抗菌活性，TxGNN 預測所捕捉的療效信號來自整個複方，Cilastatin 作為獨立再利用藥物的生物學合理性尚未建立；且香港目前無任何 Cilastatin 許可證，現有臨床試驗均為複方比較研究，缺乏針對 S. aureus 感染的設計性試驗。

**若要推進需要：**
- **釐清研究標的**：明確界定再利用對象為 Cilastatin 單方（DHP-I 抑制的非抗菌作用機轉）或 Imipenem/Cilastatin 複方的新適應症延伸
- **補充 MOA 資料**：取得 Cilastatin 對免疫調節、腎臟保護或其他非 DHP-I 相關通路的作用機轉完整資料（DrugBank API 查詢）
- **設計前瞻性研究**：針對難治性 MRSA 或 MSSA 嚴重感染（心內膜炎、骨髓炎）設計規範性臨床試驗
- **香港法規評估**：向衛生署確認以 Imipenem/Cilastatin 複方申請新適應症的可行性及所需資料包
- **安全性監測計畫**：取得完整仿單，建立包含腎功能、肝功能及神經系統（癲癇風險）的安全性監測框架
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

