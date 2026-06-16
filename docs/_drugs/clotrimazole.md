---
layout: default
title: Clotrimazole
parent: 中證據等級 (L3-L4)
nav_order: 187
evidence_level: L4
indication_count: 3
---

# Clotrimazole
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
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

# Clotrimazole：從真菌感染到痤瘡

## 一句話總結

Clotrimazole 是一種廣效局部抗黴菌藥，全球廣泛用於治療足癬（tinea pedis）、陰道念珠菌感染及口咽念珠菌感染，目前在香港尚無已登記許可證。
TxGNN 模型預測它可能對**痤瘡 (Acne)** 有效（TxGNN 全球預測排名第 3,509），
目前有 **1 個臨床試驗**涉及此方向，但 Clotrimazole 在該試驗中僅為複方輔助成分，且試驗已暫停，尚無文獻直接支持此適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 皮膚及黏膜真菌感染（足癬、陰道念珠菌感染、口咽念珠菌感染；全球常見適應症，香港尚未核准） |
| 預測新適應症 | 痤瘡 (Acne) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏正式的作用機轉（MOA）資料。根據現有文獻（PMID [24863842](https://pubmed.ncbi.nlm.nih.gov/24863842/)），Clotrimazole 是合成咪唑類抗黴菌藥，核心機轉為抑制真菌 CYP51（lanosterol 14α-demethylase），阻斷麥角固醇（ergosterol）生合成，破壞真菌細胞膜完整性，對 *Candida spp.* 及皮癬菌均具廣效抑菌活性。

TxGNN 推測 Clotrimazole 對痤瘡的潛在機轉連結有兩條間接路徑：其一，部分痤瘡（尤其脂溢性皮膚炎合併型）伴隨 *Malassezia* 屬真菌過度增殖，Clotrimazole 局部外用對 *Malassezia* 具一定抑制作用；其二，局部咪唑類藥物已有報告顯示具輕微抗炎特性，或可緩解局部炎症反應。

然而，痤瘡的核心病理機轉——皮脂腺功能亢進、*Cutibacterium acnes*（前稱 *P. acnes*）細菌菌叢失調、毛囊皮脂腺角化異常——與 Clotrimazole 的抗黴菌藥效學並無直接對應。機轉連結屬間接推測性，目前無任何文獻直接研究 Clotrimazole 單用於痤瘡的療效，臨床轉譯性待前臨床研究驗證。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | 已暫停 | 80 | 評估 Beclomethasone 0.025% + Gentamicin 0.1% + Clotrimazole 1% 三聯複方乳膏對雙側對稱性皮膚病損（含痤瘡）之比較療效；Clotrimazole 僅為輔助複方成分，非主要研究藥物，試驗已中止，無結果數據可用 |

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Clotrimazole 在香港目前無任何已登記藥品許可證（總計 0 張），屬未上市藥物，無核准適應症資料可參考。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
痤瘡適應症僅有 1 個已暫停的三聯複方試驗，Clotrimazole 非該試驗主要研究藥物，無任何文獻直接評估其對痤瘡的單藥療效，機轉連結屬間接推測，L4 證據強度不足以支持進一步推進登記。

**若要推進需要：**
- 前臨床研究：建立 *Malassezia* 相關痤瘡體外或動物模型，評估 Clotrimazole 療效
- 完整 MOA 資料補充（建議查詢 DrugBank API：DB00257）
- 設計以 Clotrimazole 為主要研究藥物的 Phase 2 探索性臨床試驗
- 取得香港衛生署藥品仿單 PDF，完成安全性初評（目前為 Blocking Data Gap）

---
---

## 補充分析：其他預測適應症

本次 Evidence Pack 另含兩項預測適應症，其中**外陰陰道炎**具有壓倒性的 L1 臨床佐證，建議優先評估市場推進可行性。

| 適應症 | TxGNN 分數 | 臨床試驗數 | 文獻數 | 證據等級 | 建議 |
|--------|-----------|-----------|--------|---------|------|
| 外陰陰道炎 (Vulvovaginitis) | 99.59% | 22 | 20 | **L1** | **Proceed with Guardrails** |
| 停經後萎縮性陰道炎 (Postmenopausal Atrophic Vaginitis) | 99.46% | 1（相關性低） | 0 | L4 | Hold |

---

### 外陰陰道炎（Vulvovaginitis）｜L1 級證據 → Proceed with Guardrails

**機轉連結：**
機轉明確且直接——Clotrimazole 藉由抑制 *Candida spp.* 的 CYP51，導致麥角固醇耗竭、細胞膜通透性喪失，對 *C. albicans* 及 non-albicans *Candida* 均有效。外陰陰道念珠菌感染（VVC）為 Clotrimazole 陰道製劑之核心全球臨床用途，機轉-疾病吻合度極高（直接靶向致病原）。此外，研究亦顯示 Clotrimazole 治療後可調節陰道菌相脂質代謝（PMID: [39419780](https://pubmed.ncbi.nlm.nih.gov/39419780/)），提供恢復健康菌相的附加機轉。

#### 主要臨床試驗（10 個最相關）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02242695](https://clinicaltrials.gov/study/NCT02242695) | Phase 4 | 已完成 | 150 | 直接頭對頭 RCT 比較 Dequalinium chloride 10mg vs **Clotrimazole 100mg** 陰道製劑治療 VVC，Clotrimazole 為主要試驗藥物之一，高直接相關性 |
| [NCT00313131](https://clinicaltrials.gov/study/NCT00313131) | Phase 3 | 已完成 | 1,524 | 大型多中心 RCT，比較 Tinidazole+Fluconazole 單劑 vs **Metronidazole+Clotrimazole** 標準療程（7 日甲硝唑 + 3 日陰道 Clotrimazole）治療西非婦女陰道感染，提供高品質療效比較基準 |
| [NCT03562156](https://clinicaltrials.gov/study/NCT03562156) | Phase 3 | 已完成 | 438 | 雙盲安慰劑對照 RCT，評估 Oteseconazole 治療復發性 VVC（RVVC）；屬最高等級 VVC 臨床證據，設計嚴謹，確認抗黴菌治療在 RVVC 中的核心地位 |
| [NCT04699240](https://clinicaltrials.gov/study/NCT04699240) | Phase 4 | 已完成 | 140 | **Clotrimazole 陰道錠** + 口服 Lactobacillus vs 單用 Clotrimazole，評估輔助益生菌對預防 VVC 復發的效果 |
| [NCT03005353](https://clinicaltrials.gov/study/NCT03005353) | Phase 2/3 | 已完成 | 100 | 孜然萃取物陰道凝膠 vs **Clotrimazole 陰道凝膠**治療念珠菌陰道炎，Clotrimazole 作為主動對照，間接確立其療效基準 |
| [NCT03599323](https://clinicaltrials.gov/study/NCT03599323) | N/A | 已完成 | 1,033 | **Empecid L Cream（Clotrimazole 1%）**上市後安全性問卷研究（PASS），提供大樣本真實世界安全性資料 |
| [NCT01335373](https://clinicaltrials.gov/study/NCT01335373) | N/A | 已完成 | 13,024 | 大型觀察性研究（Neo-Penotran Forte），n=13,024，提供 VVC 流行病學背景，確認陰道念珠菌感染為最常見婦科問題之一 |
| [NCT06835361](https://clinicaltrials.gov/study/NCT06835361) | Phase 2/3 | 招募中 | 264 | **Clotrimazole+Lactulose** 複方 vs **Clotrimazole 單方（Canesten®）**直接比較，評估組合藥物優越性；Clotrimazole 為主要比較基準 |
| [NCT03024502](https://clinicaltrials.gov/study/NCT03024502) | Phase 1/2 | 狀態不明 | 90 | EPP-AF 丙蜂膠黏附性凝膠安全性評估，**Clotrimazole 乳膏**作為主動對照，狀態不明，結果可靠性存疑 |
| [NCT02860845](https://clinicaltrials.gov/study/NCT02860845) | Phase 4 | 已完成 | 48 | 硼酸+益生菌陰道膠囊 vs 標準對照治療念珠菌感染，評估 VVC 替代管理方案，Clotrimazole 非主要研究藥物 |

#### 主要文獻（10 篇最相關）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41765149](https://pubmed.ncbi.nlm.nih.gov/41765149/) | 2026 | RCT | Complement Ther Med | 比較 Prangos ferulacea 陰道乳膏與 **Clotrimazole** 陰道乳膏治療 VVC 之臨床及實驗室療效，直接評估 Clotrimazole 療效 |
| [39824974](https://pubmed.ncbi.nlm.nih.gov/39824974/) | 2025 | 三盲 RCT | Sci Rep | 126 名患者三盲 RCT，比較 Mycozin 與 **Clotrimazole 1%** 陰道乳膏治療念珠菌陰道炎，確認 Clotrimazole 療效等效基準 |
| [30565745](https://pubmed.ncbi.nlm.nih.gov/30565745/) | 2019 | RCT | Mycoses | 益生菌+乳鐵蛋白作為 RVVC 維持治療的隨機臨床試驗，**Clotrimazole** 作為標準治療背景用藥 |
| [3895960](https://pubmed.ncbi.nlm.nih.gov/3895960/) | 1985 | RCT | Am J Obstet Gynecol | 199 名患者開放性 RCT，**Clotrimazole 500mg 單劑**對比 100mg 6 天療程治療念珠菌陰道炎，兩組療效相當 |
| [27880086](https://pubmed.ncbi.nlm.nih.gov/27880086/) | 2017 | RCT | Women Health | 三盲試驗（n=150），Calendula officinalis vs **Clotrimazole** 陰道乳膏治療陰道念珠菌感染，同時評估性功能次要指標 |
| [24863842](https://pubmed.ncbi.nlm.nih.gov/24863842/) | 2014 | 全面回顧 | J Appl Microbiol | Clotrimazole 作為藥物的過去、現在與未來：確認 VVC、足癬、口咽念珠菌感染為核心適應症，並探討新興應用潛力（包含抗腫瘤、鐮狀細胞病） |
| [2644595](https://pubmed.ncbi.nlm.nih.gov/2644595/) | 1989 | 臨床研究 | Obstet Gynecol | 前瞻雙盲 RCT（n=42），**Clotrimazole 500mg** 每週陰道栓用於復發性 VVC，90.4% 達臨床緩解，83% 達黴菌學陰性 |
| [39419780](https://pubmed.ncbi.nlm.nih.gov/39419780/) | 2024 | 機轉/微生物相研究 | J Appl Microbiol | **Clotrimazole** 治療後誘導陰道菌相組成及脂質代謝轉變，闡明 VVC 恢復健康菌相的分子機轉 |
| [1877264](https://pubmed.ncbi.nlm.nih.gov/1877264/) | 1991 | 比較研究 | DICP | Fluconazole 三日療程 vs **Clotrimazole** 陰道錠治療急性 *Candida* 陰道炎（n=185 評估），療效相當（84% vs 88% 無症狀率） |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | 臨床回顧 | J Women Health | 復發性 VVC（RVVC）管理挑戰回顧，探討 non-albicans *Candida* 對唑類藥物抗藥性問題，提供 Clotrimazole 在 RVVC 管理中的治療背景 |

#### 小結：外陰陰道炎推進建議

**決策：Proceed with Guardrails**

Clotrimazole 陰道製劑治療 VVC 之療效已獲多個 Phase 3/4 RCT 確認，為全球公認的標準治療選項（L1 級證據）。香港目前尚無已登記 Clotrimazole 許可證，具有明確的市場推進機會，尤其 Canesten® 等成熟品牌已具備完整全球安全性資料。

**若要推進需要：**
- 取得香港衛生署 / 原廠仿單 PDF，完成安全性初評（目前為 Blocking Data Gap）
- 確認陰道栓劑、乳膏、卵形製劑等劑型的適配性與給藥路徑相容性
- 評估 Canesten® 原廠品牌或學名藥的許可證申請路徑
- 制定特定族群（孕婦、免疫低下患者）的安全性監測計畫

---

### 停經後萎縮性陰道炎（Postmenopausal Atrophic Vaginitis）｜L4 級證據 → Hold

**TxGNN 分數：99.46%**　|　**臨床試驗：1 個（相關性低）**　|　**文獻：0 篇**

停經後萎縮性陰道炎（GSM/Atrophic Vaginitis）主要病理為雌激素缺乏導致陰道上皮萎縮、陰道 pH 升高（>5）、乳酸桿菌減少，核心治療為局部雌激素替代或 DHEA 補充。Clotrimazole 對萎縮性變化本身無直接作用；機轉連結屬二階間接性——若萎縮性陰道炎繼發 VVC，Clotrimazole 可作為輔助治療，但此為症狀管理而非原發疾病治療，目前無直接臨床設計支持，維持 Hold 建議。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

